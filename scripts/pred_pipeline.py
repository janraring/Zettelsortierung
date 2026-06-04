from multiprocessing import freeze_support
import os

import dotenv
import pandas as pd
from zettelsortierung import (
    Batch,
    Classifiers,
    Composition,
    DataBase,
    Flatten,
    MobileNetV3ModelSmall,
    PredictionModel,
    Scan,
    SequentialApp,
    ToDataBase,
)
from zettelsortierung.nn.datasets.parquet_dataset import ParquetDataset

dotenv.load_dotenv()


if __name__ == "__main__":
    freeze_support()

    connection_string = "sqlite:////home/jan/Dokumente/IT-Beratung Raring/Zettelsortierung/data/interim/pre-zettel.db"
    db = DataBase(connection_string=connection_string)

    root = "data/processed/Scans.parquet"
    df = pd.read_parquet(root)
    hdf = df[df["path"].str.contains("1#")]

    start = 1150000  # new_start = old_start + stride
    stride = 150000
    paths = list(hdf["path"])  # [start : start + stride]

    num_classes = 581
    num_epochs = 50
    classifier = Classifiers.MODEL_V25002_50
    root = os.getenv("PROJECT_ROOT")
    device = os.getenv("TORCH_DEVICE")
    assert root is not None
    assert device is not None

    train_set = ParquetDataset(f"{root}/data/interim/{num_classes}_classes.parquet", train=True)
    model = MobileNetV3ModelSmall.from_pretrained(
        path_str=f"{root}/models/mobile_net_v3_small_{num_classes}_classes_{num_epochs}_epochs_best",
        num_classes=num_classes,
    )
    classes = train_set.get_classes()

    def print_res(results):
        for classification in results:
            assert not isinstance(classification, Scan)
            print(
                f"{classification.zettel.id}  ->  {classification.label.sammlung.name}\t\t({classification.classifier.name}, {classification.label.confidence * 100:.2f})"  # type: ignore
            )
        return results

    pipeline = Composition(
        Batch(50000),
        SequentialApp(
            PredictionModel(
                model=model,
                device=device,
                batch_size=12,
                classifier=classifier,
                classes=classes,
            ),
            print_res,
            ToDataBase(db_adder=db.merge_classifications),
        ),
        Flatten(),
    )

    results = pipeline(paths)  # type: ignore
