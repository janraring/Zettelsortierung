import os
from pathlib import Path
from typing import Self, Sequence

from dotenv import load_dotenv
from PIL.Image import Image
import torch
import torch.nn as nn
from torchvision import models

from ..datasets.transforms import mobile_net_infer_transform
from .base import BaseModel

load_dotenv()


class MobileNetV3ModelSmall(BaseModel):
    def __init__(self, num_classes: int):
        super().__init__()
        self.model = models.mobilenet_v3_small(weights=models.MobileNet_V3_Small_Weights.DEFAULT)
        self.model.classifier[3] = nn.Linear(1024, num_classes)

    def forward(self, x):
        return self.model(x)

    def get_num_parameters(self):
        return sum(p.numel() for p in self.parameters() if p.requires_grad)

    def get_backbone_params(self):
        return self.model.features.parameters()

    def get_head_params(self):
        return self.model.classifier.parameters()

    def freeze_backbone(self):
        for param in self.model.features.parameters():
            param.requires_grad = False

    def unfreeze_backbone(self):
        for param in self.model.features.parameters():
            param.requires_grad = True

    def predict(self, images: list[Image] | Sequence[Image]) -> list[dict]:
        device = os.getenv("TORCH_DEVICE")
        tensor = torch.stack(
            [mobile_net_infer_transform(img) for img in images]  # type: ignore
        ).to(device)

        with torch.no_grad():
            logits = self(tensor)
            probs = torch.softmax(logits, dim=1)

        return [
            {
                "class": p.argmax().item(),
                "confidence": p.max().item(),
                "all_probs": p,
            }
            for p in probs
        ]

    def predict_old(self, images: list[Image] | Sequence[Image]) -> list[dict]:
        device = os.getenv("TORCH_DEVICE")
        tensor = torch.stack(
            [mobile_net_infer_transform(img) for img in images]  # type: ignore
        ).to(device)

        with torch.no_grad():
            logits = self(tensor)
            probs = torch.softmax(logits, dim=1)

        return [
            {
                "class": p.argmax().item(),
                "confidence": p.max().item(),
                "all_probs": p,
            }
            for p in probs
        ]

    @classmethod
    def from_pretrained(cls, path_str: str, num_classes) -> Self:
        path = Path(path_str)
        model = cls(num_classes=num_classes)
        device = os.getenv("TORCH_DEVICE")
        model.load_state_dict(torch.load(path / "model_weights.pt", map_location=device))
        model.to(device)
        model.eval()
        return model
