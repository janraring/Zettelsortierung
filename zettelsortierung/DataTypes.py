from dataclasses import dataclass
from typing import Any, NamedTuple, Self, Protocol
from enum import Enum
import os
import cv2
import regex as re
import pandas as pd

#####################################################################
# Scan
#####################################################################


class Scan:
    __slots__ = (
        "full_path",
        "_id",
        "_file_name",
        "_relative_path",
        "_root_path",
        "_shape",
    )

    def __init__(self, full_path: str):
        self.full_path: str = full_path
        self._id: str | None = None  # Xdd-dddddddd_d
        self._file_name: str | None = None  # dddddddd_d#Xdd_d_dd_<lemma>.jpg
        self._relative_path: str | None = None  # /Xdd_<start>_<end>/d/dd_<lemma>
        self._root_path: str | None = None  # /absolute/path/to/parant/dir
        self._shape: tuple[int, int, int] | None = None  # (w, h, c)

    @property
    def shape(self) -> tuple[int, int, int]:
        shape = self._shape
        if shape is None:
            shape = cv2.imread(self.full_path).shape
            self._shape = shape
        return shape

    @property
    def file_name(self) -> str:
        file_name = self._file_name
        if file_name is None:
            file_name = re.findall(r"[^/]+?\.jpg", self.full_path)[0]
            self._file_name = file_name
        return file_name

    @property
    def relative_path(self) -> str:
        relative_path = self._relative_path
        if relative_path is None:
            relative_path = re.findall(r"((?:[^/]+?/){3})[^/]+?\.jpg", self.full_path)[
                0
            ]
            self._relative_path = relative_path
        return relative_path

    @property
    def root_path(self) -> str:
        root_path = self._root_path
        if root_path is None:
            root_path = re.findall(r"(.+?)(?:[^/]+?/){3}[^/]+?\.jpg", self.full_path)[0]
            self._root_path = root_path
        return root_path

    @property
    def id(self) -> str:
        id = self._id
        if id is None:
            number = re.findall(r"(\d{8}_\d)#", self.full_path)[0]
            prefix = re.findall(r"zettelsammlung/(...)", self.full_path)[0]
            id = f"{prefix}-{number}"
            self._id = id
        return id

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Scan):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"Scan({self.id}, {self.relative_path})"

    def __repr__(self):
        return f"Scan({self.id}, {self.relative_path})"


#####################################################################
# Zettel
#####################################################################


# @dataclass(frozen=True)
class Zettel:
    __slots__ = ("id", "recto", "verso")

    def __init__(self, path_or_id: str, /):
        number: str = re.findall(r"(\d{8})_\d#", path_or_id)[0]
        prefix: str = re.findall(r"zettelsammlung/(...)", path_or_id)[0]

        recto_path: str = re.sub(r"_\d#", "_1#", path_or_id)
        verso_path: str = re.sub(r"_\d#", "_2#", path_or_id)

        self.id: str = f"{prefix}-{number}"
        self.recto: Scan = Scan(recto_path)
        self.verso: Scan = Scan(verso_path)

    def __eq__(self, other: object):
        if isinstance(other, Zettel):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"Zettel({self.id})"

    def __repr__(self):
        return f"Zettel({self.id})"


#####################################################################
# DataPoint
#####################################################################


@dataclass(frozen=True, slots=True)
class DataPoint:
    scan: Scan
    feature_id: int
    feature: Any

    def __iter__(self):
        yield self.scan
        yield self.feature_id
        yield self.feature


@dataclass(frozen=True, slots=True)
class DataPointBatch:
    scan_batch: list[Scan]
    feature_id_batch: list[int]
    feature_batch: Any


#####################################################################
# Base Classes
#####################################################################


class Collection(Protocol):
    def add(self, item: Zettel | DataPoint):
        pass

    def clear(self):
        pass


#####################################################################
# Zettelsammlung
#####################################################################


class Zettelsammlung(set[Zettel]):
    # __slots__ = ('sammlung',)

    def __init__(self, sammlung: set[Zettel] | list[Zettel] | None = None) -> None:
        if sammlung is None:
            sammlung = set()
        super().__init__(set(sammlung))

    @classmethod
    def from_path_list(cls, paths: list[str]) -> Self:
        sammlung = {Zettel(path) for path in paths}
        return cls(sammlung)

    @classmethod
    def from_disc(cls, root: str = "", k: int = -1) -> Self:
        """
        Given a root directory, this function collects all .jpg
        files found in the subdirectories of root. Those files
        are returned as a Zettelsammlung.
        Optionally, one can specify a maximum number of Zettel k
        that should be collected.

        Args:
            root (str): Path to the root directory.
            k (int): Limit on number of Zettel to be collected.
        """
        # root = os.getenv('ZETTELSAMMLUNG_ROOT')
        file_paths: list[str] = []
        for path, _, files in os.walk(root):
            for name in files:
                if len(file_paths) == k:
                    break
                if name[-4:] == ".jpg":
                    file_paths.append(os.path.join(path, name))
            else:
                continue
            break
        return cls.from_path_list(file_paths)

    @classmethod
    def from_parquet(cls, path: str, k: int | None = None) -> Self:
        file_paths_df = pd.read_parquet(path)
        file_paths = file_paths_df["path"].to_list()[:k]
        return cls.from_path_list(file_paths)

    def to_parquet(self, path: str):
        file_paths: list[str] = [zettel.recto.full_path for zettel in self]
        file_paths_df = pd.DataFrame({"path": file_paths})
        file_paths_df.to_parquet(path)


#####################################################################
# Bounding Box
#####################################################################


class BoundingBox(NamedTuple):
    x: int
    y: int
    w: int
    h: int


@dataclass(frozen=True, slots=True)
class Probe(list[DataPoint]):
    def __init__(self, probe: list[DataPoint] | None = None):
        if probe is None:
            probe = []
        super().__init__(probe)

    def add(self, item: DataPoint) -> None:
        self.append(item)

    def add_batch(self, data_points: list[DataPoint]) -> None:
        self.extend(data_points)

    def __repr__(self):
        repr = "Probe(["
        for i in range(min(100, len(self))):
            repr += str(self[i]) + ",\n"
        return repr + "...])"


#####################################################################
# Classification
#####################################################################


class Classifiers(Enum):
    GOLD = "Grundwahrheit"
    OCR = "OCR-Auslesung"


class TopCategory(Enum):
    SKIP = "skipped"
    LAUTSCHRIFT = "Lautschrift"
    FRAGEBOGEN = "Fragebogen"
    WORTSCHATZ = "Wortschatz"
    EXZERPT = "Exzerpt"
    SONSTIGE = "Sonstige"
