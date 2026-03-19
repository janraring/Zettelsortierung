from abc import ABC, abstractmethod
from typing import Iterator
import torch.nn as nn
from torch.nn.parameter import Parameter


class BaseModel(ABC, nn.Module):
    @abstractmethod
    def get_num_parameters(self) -> int: ...

    @abstractmethod
    def get_backbone_params(self) -> Iterator[Parameter]: ...

    @abstractmethod
    def get_head_params(self) -> Iterator[Parameter]: ...

    @abstractmethod
    def freeze_backbone(self) -> None: ...

    @abstractmethod
    def unfreeze_backbone(self) -> None: ...
