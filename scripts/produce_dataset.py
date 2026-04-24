import os

import pandas as pd
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split

from zettelsortierung.db import DataBase
from zettelsortierung import Classifiers
from zettelsortierung import Sammlungen

load_dotenv()

TEST_SIZE = 0.1


def main():
    db = DataBase()

    classifications = db.get_classifications(Classifiers.MANUELL)

    ids = []
    labels = []

    for key, value in classifications.items():
        if value.sammlung.name not in [
            "SKIPPED",
            "OA",
            "LST_RUE",
            "BUER_TUE",
            "OLPE_HB",
            "WML_BB",
        ]:
            ids.append(key)
            labels.append(value.sammlung.name)

    x_train, x_test, y_train, y_test = train_test_split(
        ids, labels, test_size=TEST_SIZE, stratify=labels
    )

    x = x_train + x_test
    y = y_train + y_test
    train = [True] * len(x_train) + [False] * len(x_test)

    df = pd.DataFrame({"zettel_id": x, "class": y, "train": train})

    num_classes = len(set(labels))
    root = os.getenv("PROJECT_ROOT")
    target = f"{root}/data/interim/{num_classes}_classes.parquet"

    df.to_parquet(target)

    print(f"Number of classes: {num_classes}")
    print(f"Number of examples: {len(df)}")


if __name__ == "__main__":
    main()
