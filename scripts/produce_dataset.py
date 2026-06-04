from collections import Counter
import os

from dotenv import load_dotenv
import pandas as pd
from sklearn.model_selection import train_test_split
from zettelsortierung import Classifiers
from zettelsortierung.db import DataBase

load_dotenv()

TEST_SIZE = 0.1


def main():
    db = DataBase()

    classifications = db.get_classifications(Classifiers.MANUELL)

    ids = []
    labels = []

    # Create list of ids and labels, filter out `SKIPPED` and `OA`
    for key, value in classifications.items():
        if value.sammlung.name not in [
            "SKIPPED",
            "OA",
        ]:
            ids.append(key)
            labels.append(value.sammlung.name)

    # Filter out those categories that only contain one Zettel
    counts = Counter(labels)
    ids, labels = zip(*((id_, label) for id_, label in zip(ids, labels) if counts[label] > 1))

    # Create train/test split
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
