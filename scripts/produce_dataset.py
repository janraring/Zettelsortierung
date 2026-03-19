import os

import pandas as pd
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split

from zettelsortierung.db import DataBase
from zettelsortierung import Classifiers

load_dotenv()


def load_df(path):
    df = pd.read_parquet(path)
    print(f"Loaded {len(df)} rows.")
    return df


def main():
    db = DataBase()
    root = os.getenv("PROJECT_ROOT")
    target = f"{root}/data/interim/class_112x60.parquet"

    classifications = db.get_classifications(Classifiers.MANUELL)

    ids = []
    labels = []

    for key, value in classifications.items():
        if value.sammlung.name not in ["SKIPPED", "VERWEIS"]:
            ids.append(key)
            labels.append(value.sammlung.name)

    x_train, x_test, y_train, y_test = train_test_split(
        ids, labels, test_size=0.2, stratify=labels
    )

    x = x_train + x_test
    y = y_train + y_test
    train = [True] * len(x_train) + [False] * len(x_test)

    df = pd.DataFrame({"zettel_id": x, "class": y, "train": train})

    df.to_parquet(target)
    load_df(target)


if __name__ == "__main__":
    main()
