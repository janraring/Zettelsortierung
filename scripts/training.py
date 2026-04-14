import os
import argparse
from dotenv import load_dotenv
from zettelsortierung.nn import (
    ParquetDataset,
    TrainingConfig,
    Trainer,
    MobileNetV3ModelSmall,
)

load_dotenv()


def run_training(dataset_name: str, num_epochs: int | None = None):
    root = os.getenv("PROJECT_ROOT")
    if root is None:
        root = ""
    data_path = root + f"/data/interim/{dataset_name}.parquet"

    train_set = ParquetDataset(data_path, train=True)
    test_set = ParquetDataset(data_path, train=False)
    num_classes = len(train_set.get_classes())
    model = MobileNetV3ModelSmall(num_classes)

    config = TrainingConfig(num_classes)
    if num_epochs is not None:
        config.num_epochs = num_epochs

    trainer = Trainer(
        model=model, train_set=train_set, test_set=test_set, config=config
    )
    trainer.train()

    name = f"mobile_net_v3_small_{config.num_epochs}ep_on_{dataset_name}"
    trainer.save(f"{root}/models/{name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Trains a MobileNetV3ModelSmall on the specified dataset with the given parameters."
    )
    parser.add_argument("--dataset", required=True, type=str)
    parser.add_argument("--epochs", required=False, type=int, default=None)
    args = parser.parse_args()

    dataset_name = args.dataset
    num_epochs = args.epochs

    run_training(dataset_name, num_epochs)
