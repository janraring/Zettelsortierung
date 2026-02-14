from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, NamedTuple, Self
import regex as re
import os
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
# Zettelwerk
#####################################################################

@dataclass(frozen=True, slots=True)
class Zettel:
    seed_file_path: str

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

    def __eq__(self, other):
        return self.recto_file_path == other.recto_file_path
    
    def __hash__(self):
        return hash(self.recto_file_path)
    
    def __str__(self):
        return f'Zettel({self.id})'

    def __repr__(self):
        return f'Zettel({self.id})'


class Zettelsammlung(set, Collection):
    def __init__(self, sammlung: set[Zettel] | list[Zettel] | None = None):
        if sammlung is None:
            sammlung = {}
        super().__init__(set(sammlung))
    
    @staticmethod
    def from_path_list(paths: list[str]) -> Self:
        sammlung = [Zettel(path) for path in paths]
        return Zettelsammlung(sammlung)

    @classmethod
    def from_disc(cls, root: str, k: int=-1) -> Self:
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
    zettel_id: str
    feature_id: int
    feature: Any


#class Probe(Collection):
@dataclass(frozen=True)
class Probe(list, Collection):
    def __init__(self, probe: list[DataPoint] | None = None):
        if probe is None:
            probe = {}
        super().__init__(list(probe))
    #data_points: list[DataPoint] = field(default_factory=list)

#    def __iter__(self):
#        for data_point in self.data_points:
#            yield data_point
#
    def add(self, data_point: DataPoint):
        self.append(data_point)
    
    def add_batch(self, data_points: list[DataPoint]):
        self.extend(data_points)
    
    def clear(self):
        self = []

    def to_parquet(self):
        ...
    
    @staticmethod
    def from_parquet():
        ...