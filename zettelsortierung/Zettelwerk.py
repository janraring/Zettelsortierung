import os
import regex as re
import pandas as pd
from dotenv import load_dotenv
from dataclasses import dataclass
from tqdm import tqdm
from typing import Self

load_dotenv()


@dataclass
class Zettel:
    def __init__(self, _file_path: str, /):
        '''
        Container for a Belegzettel.
        
        :param _file_path: The absolute path of the directory where
        all the images live.
        :type _file_path: str
        '''
        self._file_path = _file_path

    @property
    def recto_file_path(self) -> str:
        return re.sub(r'_\d#', '_1#', self._file_path)

    @property
    def verso_file_path(self) -> str:
        return re.sub(r'_\d#', '_2#', self._file_path)

    @property
    def recto_file_name(self) -> str:
        return re.findall(r'(gpj\..+?)/', self.recto_file_path[::-1])[0][::-1]

    @property
    def verso_file_name(self) -> str:
        return re.findall(r'(gpj\..+?)/', self.verso_file_path[::-1])[0][::-1]
    
    @property
    def parent_folder(self) -> str:
        return re.findall(r'(?:/[\w-]+){3}', self.recto_file_path[::-1])[0][::-1]
    
    @property
    def number(self) -> str:
        return self.recto_file_name[:8]

    def __eq__(self, other):
        return self.recto_file_path == other.recto_file_path
    
    def __hash__(self):
        return hash(self.recto_file_path)
    
    def __str__(self):
        return self.recto_file_name

    def __repr__(self):
        return self.recto_file_name
    


class Zettelsammlung(set):
    def __init__(self, sammlung: set[Zettel] | list[Zettel]=None):
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


if __name__ == '__main__':
    root = os.getenv('ZETTELSAMMLUNG_ROOT')
    sammlung = Zettelsammlung.from_disc(root, 40000)
    print(len(sammlung))

    path = 'data/interim/test_path_collection.parquet'
    sammlung.to_parquet(path)
    sammlung = Zettelsammlung.from_parquet(path)
    print(len(sammlung))