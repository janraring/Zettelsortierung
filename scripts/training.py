import os
from dotenv import load_dotenv
from zettelsortierung.nn import (
    SixtySamples,
    ParquetDataset,
    TrainingConfig,
    Trainer,
    MobileNetV3ModelSmall,
)

load_dotenv()


def main():
    root = os.getenv("PROJECT_ROOT")
    if root is None:
        root = ""
    dataset_name = "136_classes"
    data_path = root + f"/data/interim/{dataset_name}.parquet"

    train_set = ParquetDataset(data_path, train=True)
    test_set = ParquetDataset(data_path, train=False)
    num_classes = len(train_set.get_classes())
    config = TrainingConfig(num_classes)
    model = MobileNetV3ModelSmall(num_classes)
    trainer = Trainer(
        model=model, train_set=train_set, test_set=test_set, config=config
    )
    trainer.train()

    # path = os.getenv("PROJECT_ROOT")
    name = f"mobile_net_v3_small_{config.num_epochs}ep_on_{dataset_name}"
    # name = "mobile_net_v3_small_20ep_on_sixty_samples"
    trainer.save(f"{root}/models/{name}")


if __name__ == "__main__":
    main()
