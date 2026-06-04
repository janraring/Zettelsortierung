from abc import ABC, abstractmethod

from torch.utils.data import Dataset


class BaseDocumentDataset(ABC, Dataset):
    @abstractmethod
    def get_classes(self) -> list[str]: ...

    @abstractmethod
    def get_idx_to_class(self) -> dict[int, str]: ...

    @abstractmethod
    def get_class_to_idx(self) -> dict[str, int]: ...

    @abstractmethod
    def get_transform(self): ...
