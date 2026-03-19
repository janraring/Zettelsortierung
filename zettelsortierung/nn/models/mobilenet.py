from torchvision import models
import torch.nn as nn
from .base import BaseModel


class MobileNetV3ModelSmall(BaseModel):
    def __init__(self, num_classes: int):
        super().__init__()
        self.model = models.mobilenet_v3_small(
            weights=models.MobileNet_V3_Small_Weights.DEFAULT
        )
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
