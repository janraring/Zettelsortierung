from abc import ABC, abstractmethod
from dataclasses import dataclass
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

#@dataclass(frozen=True)
class Scan:
    __slots__ = ('full_path',
                 '_id',
                 '_file_name',
                 '_relative_path',
                 '_root_path',
                 '_shape')

    def __init__(self, full_path: str):
        self.full_path = full_path
        self._id = None             # Xdd-dddddddd_d
        self._file_name = None      # dddddddd_d#Xdd_d_dd_<lemma>.jpg
        self._relative_path = None  # /Xdd_<start>_<end>/d/dd_<lemma>
        self._root_path = None      # /absolute/path/to/parant/dir
        self._shape = None          # (w, h, c)

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
            file_name = re.findall(r'[^/]+?\.jpg', self.full_path)[0]
            self._file_name = file_name
        return file_name

    @property
    def relative_path(self) -> str:
        relative_path = self._relative_path
        if relative_path is None:
            relative_path = \
                re.findall(r'((?:[^/]+?/){3})[^/]+?\.jpg',
                           self.full_path)[0]
            self._relative_path = relative_path
        return relative_path

    @property
    def root_path(self) -> str:
        root_path = self._root_path
        if root_path is None:
            root_path = \
                re.findall(r'(.+?)(?:[^/]+?/){3}[^/]+?\.jpg',
                self.full_path)[0]
            self._root_path = root_path
        return root_path

    @property
    def id(self) -> str:
        id = self._id
        if id is None:
            number = re.findall(r'(\d{8}_\d)#', self.full_path)[0]
            prefix = re.findall(r'zettelsammlung/(...)',
                                self.full_path)[0]
            id = f'{prefix}-{number}'
            self._id = id
        return id

    def __eq__(self, other):
        return self.id == other.id
    
    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f'Scan({self.id, self.full_path})'

    def __repr__(self):
        return f'Scan({self.id, self.full_path})'


#####################################################################
# Zettel
#####################################################################

#@dataclass(frozen=True)
class Zettel:
    __slots__ = ('id', 'recto', 'verso')

    def __init__(self, path, /):
        number = re.findall(r'(\d{8})_\d#', path)[0]
        prefix = re.findall(r'zettelsammlung/(...)', path)[0]

        recto_path = re.sub(r'_\d#', '_1#', path)
        verso_path = re.sub(r'_\d#', '_2#', path)

        self.id = f'{prefix}-{number}'
        self.recto = Scan(recto_path)
        self.verso = Scan(verso_path)

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
    __slots__ = ('sammlung')

    def __init__(self,
                 sammlung: set[Zettel] | list[Zettel] | None = None):
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
        #root = os.getenv('ZETTELSAMMLUNG_ROOT')
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
        file_paths = file_paths_df['path'].to_list()[:k]
        return cls.from_path_list(file_paths)

    def to_parquet(self, path):
        file_paths = [zettel.recto_file_path for zettel in self]
        file_paths_df = pd.DataFrame({'path': file_paths})
        file_paths_df.to_parquet(path)


#####################################################################
# Bounding Box
#####################################################################

class BoundingBox(NamedTuple):
    x: int
    y: int
    w: int
    h: int


#####################################################################
# Feature Extraction
#####################################################################

@dataclass(frozen=True, slots=True)
class DataPoint():
    zettel: Zettel
    feature_id: int
    feature: Any

    def __iter__(self):
        yield self.zettel
        yield self.feature_id
        yield self.feature


@dataclass(frozen=True, slots=True)
class DataPointBatch():
    zettel_batch: list[Zettel]
    feature_id_batch: list[int]
    feature_batch: Any


@dataclass(frozen=True)
class Probe(list, Collection):
    __slots__ = ('probe')

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