from pathlib import Path
import time
import os
from dotenv import load_dotenv

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm
import numpy as np

from ..models.base import BaseModel
from ..datasets.base import BaseDocumentDataset
from ..config import TrainingConfig

load_dotenv()


class Trainer:
    def __init__(
        self,
        model: BaseModel,
        train_set: BaseDocumentDataset,
        test_set: BaseDocumentDataset,
        config: TrainingConfig,
    ):
        self.model = model.to(config.device)
        self.config = config
        self.device = torch.device(config.device)

        self.train_set = train_set
        self.test_set = test_set
        self.train_loader = self._get_dataloader(train_set, config, train=True)
        self.test_loader = self._get_dataloader(test_set, config, train=False)

        self.criterion = nn.CrossEntropyLoss(label_smoothing=0.1)
        self.optimizer = torch.optim.AdamW(
            filter(lambda p: p.requires_grad, model.parameters()),
            lr=config.learning_rate,
            weight_decay=0.05,
        )
        self.scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            self.optimizer, T_max=config.num_epochs
        )

        self.best_val_acc = 0.0
        self.writer: SummaryWriter = SummaryWriter()
        self.history: list[dict] = []

    @staticmethod
    def _get_dataloader(
        dataset: BaseDocumentDataset, config, *, train: bool
    ) -> DataLoader:
        return DataLoader(
            dataset,
            batch_size=config.batch_size,
            shuffle=train,
            num_workers=config.num_workers,
            pin_memory=config.pin_memory,
        )

    # --------------------------------------------------------------------

    def train(self):
        print("Phase 1: training head only")
        self.model.freeze_backbone()
        self._run_epochs(0, self.config.num_epochs // 2)

        print("Phase 2: fine-tuning full model")
        self.model.unfreeze_backbone()
        self.optimizer = torch.optim.AdamW(
            [
                {
                    "params": self.model.get_backbone_params(),
                    "lr": self.config.learning_rate / 10,
                },
                {
                    "params": self.model.get_head_params(),
                    "lr": self.config.learning_rate,
                },
            ]
        )
        warmup = torch.optim.lr_scheduler.LinearLR(
            self.optimizer, start_factor=0.1, end_factor=1.0, total_iters=3
        )
        cosine = torch.optim.lr_scheduler.CosineAnnealingLR(
            self.optimizer, T_max=(self.config.num_epochs // 2) - 3
        )
        self.scheduler = torch.optim.lr_scheduler.SequentialLR(
            self.optimizer, schedulers=[warmup, cosine], milestones=[3]
        )

        self._run_epochs(self.config.num_epochs // 2, self.config.num_epochs // 2)
        self.writer.flush()
        self.writer.close()

    def _run_epochs(self, start_epoch: int, num_epochs: int):
        for epoch in range(num_epochs):
            t0 = time.time()

            train_loss, train_acc = self._train_epoch()
            # val_loss, val_acc, _, _, _ = self._eval_epoch(self.test_loader)
            val_loss, val_acc = self._eval_epoch(self.test_loader)
            self.scheduler.step()

            elapsed = time.time() - t0
            self.history.append(
                {
                    "train_loss": train_loss,
                    "train_acc": train_acc,
                    "val_loss": val_loss,
                    "val_acc": val_acc,
                }
            )
            self.writer.add_scalar("loss/train", train_loss, start_epoch + epoch + 1)
            self.writer.add_scalar("loss/val", val_loss, start_epoch + epoch + 1)
            self.writer.add_scalar("acc/train", train_acc, start_epoch + epoch + 1)
            self.writer.add_scalar("acc/val", val_acc, start_epoch + epoch + 1)

            print(
                f"Epoch {start_epoch + epoch + 1}/{start_epoch + num_epochs} — "
                f"train loss: {train_loss:.4f}, acc: {train_acc:.3f} | "
                f"val loss: {val_loss:.4f}, acc: {val_acc:.3f} | "
                f"{elapsed:.1f}s"
            )

            if val_acc > self.best_val_acc:
                root = os.getenv("PROJECT_ROOT")
                name = f"mobile_net_v3_small_{len(self.train_set.get_classes())}_classes_{self.config.num_epochs}_epochs_best"
                self.best_val_acc = val_acc
                self.save(f"{root}/models/{name}")

    def _mixup_batch(self, images, labels, alpha=0.3):
        lam = np.random.beta(alpha, alpha)
        idx = torch.randperm(images.size(0), device=images.device)
        mixed = lam * images + (1 - lam) * images[idx]
        return mixed, labels, labels[idx], lam

    def _train_epoch(self):
        self.model.train()
        total_loss, correct, total = 0.0, 0.0, 0
        for images, labels in tqdm(self.train_loader):
            images, labels = images.to(self.device), labels.to(self.device)
            mixed, labels_a, labels_b, lam = self._mixup_batch(images, labels)
            self.optimizer.zero_grad()
            logits = self.model(mixed)
            loss = lam * self.criterion(logits, labels_a) + (1 - lam) * self.criterion(
                logits, labels_b
            )
            loss.backward()
            self.optimizer.step()
            total_loss += loss.item() * len(labels)
            # Accuracy under mixup is approximate; use the dominant label
            correct += (logits.argmax(dim=1) == labels_a).sum().item()
            total += len(labels)
        return total_loss / total, correct / total

    # --------------------------------------------------------------------

    def _eval_epoch(self, loader: DataLoader) -> tuple[float, float]:
        self.model.eval()
        eval_criterion = nn.CrossEntropyLoss()
        total_loss, correct, total = 0.0, 0.0, 0
        with torch.no_grad():
            for images, labels in tqdm(loader):
                images, labels = images.to(self.device), labels.to(self.device)
                logits = self.model(images)
                loss = eval_criterion(logits, labels)
                total_loss += loss.item() * len(labels)
                correct += (logits.argmax(dim=1) == labels).sum().item()
                total += len(labels)
        return total_loss / total, correct / total

    # --------------------------------------------------------------------

    def save(self, path_str: str):
        path = Path(path_str)
        path.mkdir(parents=True, exist_ok=True)

        torch.save(
            {
                "model_state": self.model.state_dict(),
                "optimizer_state": self.optimizer.state_dict(),
                "scheduler_state": self.scheduler.state_dict(),
                "history": self.history,
                "confing": self.config,
            },
            path / "checkpoint.pt",
        )

        # Separate inference-only export
        torch.save(self.model.state_dict(), path / "model_weights.pt")

        # ONNX export for fast inference
        self._export_onnx(path / "model.onnx")

    def load(self, path_str: str, inference_only: bool = False):
        path = Path(path_str)
        if inference_only:
            self.model.load_state_dict(torch.load(path / "model_weights.pt"))
        else:
            checkpoint = torch.load(f"{path}/checkpoint.pt")
            self.model.load_state_dict(checkpoint["model_state"])
            self.optimizer.load_state_dict(checkpoint["optimizer_state"])
            self.scheduler.load_state_dict(checkpoint["scheduler_state"])
            self.history = checkpoint["history"]

    def _export_onnx(self, path: Path):
        import torch.onnx

        dummy = torch.randn(
            1, 3, self.config.input_size, self.config.input_size, device=self.device
        )

        self.model.eval()
        torch.onnx.export(
            self.model,
            (dummy,),
            path,
            input_names=["image"],
            output_names=["logits"],
            dynamic_axes={"image": {0: "batch_size"}, "logits": {0: "batch_size"}},
            opset_version=17,
        )

    # --------------------------------------------------------------------
