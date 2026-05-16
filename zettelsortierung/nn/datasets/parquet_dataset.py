import os

import pandas as pd
from PIL import Image

from zettelsortierung.nn.datasets.base import BaseDocumentDataset
from zettelsortierung.nn.datasets.transforms import mobile_net_aggr_transform
from zettelsortierung.db import DataBase

from dotenv import load_dotenv

db = DataBase()


class ParquetDataset(BaseDocumentDataset):
    def __init__(self, path: str, train: bool):
        self.full_df = pd.read_parquet(path)
        self.df = self.full_df[self.full_df["train"] == train]
        self.transform = mobile_net_aggr_transform
        self.classes = self.get_classes()
        self.class_to_idx = {c: i for i, c in enumerate(self.classes)}
        self.idx_to_class = {i: c for i, c in enumerate(self.classes)}

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        (zettel,) = db.get_zettels_by_ids([row["zettel_id"]])
        img = Image.open(zettel.recto.full_path).convert("RGB")
        transformed = self.transform(img)
        class_idx = self.class_to_idx[row["class"]]
        return transformed, class_idx

    def get_classes(self) -> list[str]:
        classes_col = self.full_df["class"]
        classes_set = set(classes_col)
        classes_lst = list(classes_set)
        return sorted(classes_lst)

    def get_class_to_idx(self) -> dict[str, int]:
        return self.class_to_idx

    def get_idx_to_class(self) -> dict[int, str]:
        return self.idx_to_class

    def get_transform(self):
        return self.transform


def main():
    pass


if __name__ == "__main__":
    main()
