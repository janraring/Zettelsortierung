from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from typing import Any, NamedTuple, Self
import os
import cv2
import regex as re
import pandas as pd


#####################################################################
# Base Classes
#####################################################################

class Collection(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def clear(self):
        pass


#####################################################################
# Scan
#####################################################################

@dataclass(frozen=True)
class Scan:
    id: str                 # dddddddd_d
    file_name: str          # dddddddd_d#Xdd_d_dd_<lemma>.jpg
    relative_path: str      # /Xdd_<start>_<end>/d/dd_<lemma>
    root_path: str          # /absolute/path/to/parant/directory

    @cached_property
    def full_path(self) -> str:
        return os.path.join(self.root_path,
                            self.relative_path,
                            self.file_name)

    @cached_property
    def shape(self) -> tuple[int, int, int]:
        return cv2.imread(self.full_path).shape
    
    def __str__(self):
        return f'Scan({self.id, self.full_path})'

    def __repr__(self):
        return f'Scan({self.id, self.full_path})'

    @staticmethod
    def from_path(path: str):
        id = re.findall(r'(\d{8}_\d)#', path)[0]
        file_name = re.findall(r'[^/]+?\.jpg', path)[0]
        relative_path = re.findall(r'((?:[\w-]+?/){3})[^/]+?\.jpg', path)[0]
        root_path = re.findall(r'(.+?)(?:[\w-]+?/){3}[^/]+?\.jpg', path)[0]
        return Scan(id, file_name, relative_path, root_path)


#####################################################################
# Zettel
#####################################################################

#@dataclass(frozen=True)
class Zettel:
    def __init__(self, path, /):
        recto_path = re.sub(r'_\d#', '_1#', path)
        verso_path = re.sub(r'_\d#', '_2#', path)
        self.id = re.findall(r'(\d{8})_\d#', path)[0]
        self.recto = Scan.from_path(recto_path)
        self.verso = Scan.from_path(verso_path)

    """
    @property
    def recto_file_path(self) -> str:
        return re.sub(r'_\d#', '_1#', self.seed_file_path)

    @property
    def verso_file_path(self) -> str:
        return re.sub(r'_\d#', '_2#', self.seed_file_path)

    @property
    def recto_file_name(self) -> str:
        return re.findall(r'(gpj\..+?)/', self.recto_file_path[::-1])[0][::-1]

    @property
    def verso_file_name(self) -> str:
        return re.findall(r'(gpj\..+?)/', self.verso_file_path[::-1])[0][::-1]
    
    @property
    def parent_directory(self) -> str:
        return re.findall(r'(?:/[\w-]+){3}', self.recto_file_path[::-1])[0][::-1]
    
    @property
    def id(self) -> str:
        return self.recto_file_name[:8]

    @cached_property
    def shape(self) -> tuple[int, int]:
        return cv2.imread(self.recto_file_path).shape
    """
    def __eq__(self, other):
        return self.id == other.id
    
    def __hash__(self):
        return hash(self.id)
    
    def __str__(self):
        return f'Zettel({self.id})'

    def __repr__(self):
        return f'Zettel({self.id})'


#####################################################################
# Zettelsammlung
#####################################################################

class Zettelsammlung(set, Collection):
    def __init__(self, sammlung: set[Zettel] | list[Zettel] | None = None):
        if sammlung is None:
            sammlung = {}
        super().__init__(set(sammlung))
    
    @staticmethod
    def from_path_list(paths: list[str]) -> Self:
        sammlung = {Zettel(path) for path in paths}
        return Zettelsammlung(sammlung)

    @classmethod
    def from_disc(cls, root: str='', k: int=-1) -> Self:
        '''
        Given a root directory, this function collects all .jpg
        files found in the subdirectories of root. Those files
        are returned as a Zettelsammlung.
        Optionally, one can specify a maximum number of Zettel k
        that should be collected.

        Args:
            root (str): Path to the root directory.
            k (int): Limit on number of Zettel to be collected.
        '''
        root = os.getenv('ZETTELSAMMLUNG_ROOT')
        file_paths = []
        for path, subdirs, files in os.walk(root):
            for name in files:
                if len(file_paths) == k:
                    break
                if name[-4:] == '.jpg':
                    file_paths.append(os.path.join(path, name))
            else:
                continue
            break
        return cls.from_path_list(file_paths)
    
    @classmethod
    def from_parquet(cls, path: str, k: int=None):
        file_paths_df = pd.read_parquet(path)
        file_paths = file_paths_df['file_path'].to_list()[:k]
        return cls.from_path_list(file_paths)

    def to_parquet(self, path):
        file_paths = [zettel.recto_file_path for zettel in self]
        file_paths_df = pd.DataFrame({'file_path': file_paths})
        file_paths_df.to_parquet(path)


#####################################################################
# Image Processing
#####################################################################

class BoundingBox(NamedTuple):
    x: int
    y: int
    w: int
    h: int


#####################################################################
# Data Processing
#####################################################################

@dataclass(frozen=True, slots=True)
class DataPoint():
    zettel: Zettel
    feature_id: int
    feature: Any


@dataclass(frozen=True, slots=True)
class DataPointBatch():
    zettel_batch: list[Zettel]
    feature_id_batch: list[int]
    feature_batch: Any


@dataclass(frozen=True)
class Probe(list, Collection):
    def __init__(self, probe: list[DataPoint] | None = None):
        if probe is None:
            probe = []
        super().__init__(probe)
    
    def add(self, data_point: DataPoint):
        self.append(data_point)
    
    def add_batch(self, data_points: list[DataPoint]):
        self.extend(data_points)
    
    def to_parquet(self):
        ...
    
    @staticmethod
    def from_parquet():
        ...
    
    def __repr__(self):
        repr = 'Probe(['
        for i in range(min(100, len(self))):
            repr += str(self[i]) + ',\n'
        return repr + '...])'