from pathlib import Path
from dataclasses import dataclass, field
import time

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

from ..models.base import BaseModel
from ..datasets.base import BaseDocumentDataset
from ..config import TrainingConfig
from .metrics import compute_metrics


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

        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = torch.optim.AdamW(
            filter(lambda p: p.requires_grad, model.parameters()),
            lr=config.learning_rate,
        )
        self.scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            self.optimizer, T_max=config.num_epochs
        )

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
        self._run_epochs(self.config.num_epochs // 2)

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
        self.scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            self.optimizer, T_max=self.config.num_epochs // 2
        )
        self._run_epochs(self.config.num_epochs // 2)
        self.writer.flush()
        self.writer.close()

    def _run_epochs(self, num_epochs: int):
        for epoch in range(num_epochs):
            t0 = time.time()

            train_loss, train_acc = self._train_epoch()
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
            self.writer.add_scalar("loss/train", train_loss, epoch + 1)
            self.writer.add_scalar("loss/val", val_loss, epoch + 1)
            self.writer.add_scalar("acc/train", train_acc, epoch + 1)
            self.writer.add_scalar("acc/val", val_acc, epoch + 1)

            print(
                f"Epoch {epoch+1}/{num_epochs} — "
                f"train loss: {train_loss:.4f}, acc: {train_acc:.3f} | "
                f"val loss: {val_loss:.4f}, acc: {val_acc:.3f} | "
                f"{elapsed:.1f}s"
            )

    def _train_epoch(self) -> tuple[float, float]:
        self.model.train()
        total_loss, correct, total = 0.0, 0.0, 0

        for images, labels in tqdm(self.train_loader):
            images, labels = images.to(self.device), labels.to(self.device)

            self.optimizer.zero_grad()
            logits = self.model(images)
            loss = self.criterion(logits, labels)
            loss.backward()
            self.optimizer.step()

            total_loss += loss.item() * len(labels)
            correct += (logits.argmax(dim=1) == labels).sum().item()
            total += len(labels)

        return total_loss / total, correct / total

    # --------------------------------------------------------------------

    def evaluate(self) -> dict:
        loss, acc = self._eval_epoch(self.test_loader)

        all_preds, all_labels, all_probs = [], [], []
        self.model.eval()
        with torch.no_grad():
            for images, labels in self.test_loader:
                images = images.to(self.device)
                logits = self.model(images)
                probs = torch.softmax(logits / self.config.temperature, dim=1)

                all_probs.append(probs.cpu())
                all_preds.append(probs.argmax(dim=1).cpu())
                all_labels.append(labels)

        all_preds = torch.cat(all_preds)
        all_labels = torch.cat(all_labels)
        all_probs = torch.cat(all_probs)

        # Flag low-confidence predicitons as unknown
        max_probs = all_probs.max(dim=1).values
        unknown_mask = max_probs < self.config.confidence_threshold

        metrics = compute_metrics(
            all_preds,
            all_labels,
            unknown_mask,
            idx_to_class=self.test_set.get_idx_to_class(),
        )
        metrics.update({"loss": loss, "accuracy": acc})
        return metrics

    def _eval_epoch(self, loader: DataLoader) -> tuple[float, float]:
        self.model.eval()
        total_loss, correct, total = 0.0, 0.0, 0

        with torch.no_grad():
            for images, labels in loader:
                images, labels = images.to(self.device), labels.to(self.device)
                logits = self.model(images)
                loss = self.criterion(logits, labels)

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
