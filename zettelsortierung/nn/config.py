from dataclasses import dataclass


@dataclass
class TrainingConfig:
    num_classes: int
    batch_size: int = 16
    learning_rate: float = 1e-3
    num_epochs: int = 30
    input_size: int = 384
    confidence_threshold: float = 0.7
    temperature: float = 2.0
    device: str = "xpu"
    pin_memory: bool = True
    num_workers: int = 12
