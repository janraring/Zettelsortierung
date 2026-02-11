import os
import regex as re
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
        return re.findall(r'(?:/\w+){3}', self.recto_file_path[::-1])[0][::-1]
    
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
    

class Zettelsammlung(list):
    def __init__(self, sammlung: list[Zettel]=None):
        if sammlung is None:
            sammlung = []
        super().__init__(list(set(sammlung)))

    def append(self, new_zettel):
        if new_zettel not in self:
            super().append(new_zettel)

    def extend(self, other):
        for zettel in other:
            self.append(zettel)
    
    
    @staticmethod
    def collect_zettel(root: str, k: int=0) -> Self:
        '''
        Given a root directory, this function collects all .jpg
        files found in the subdirectories of root. Those files
        are returned as a Zettelsammlung. Optionally, one can
        specify a maximum number of Zettel k that should be
        collected.
        
        :param root: Path to the root directory
        :type root: str
        :param k: Maximal number of Zettel to collect
        :type k: int
        :return: A collection of Zettel (Zettelsammlung)
        :rtype: Zettelsammlung
        '''
        if k != 0:
            sammlung = Zettelsammlung()
        else:
            sammlung = []

        for path, subdirs, files in tqdm(os.walk(root)):
            for name in files:
                if name[-4:] == '.jpg':
                    new_zettel = Zettel(os.path.join(path, name))
                    sammlung.append(new_zettel)
                    if len(sammlung) == k:
                        break
            else:
                continue
            # We only land here if the break the loop, i.e. if a
            # maximum number of Zettel has been set, but if this
            # is the case, then `sammlung` was initialized as a
            # `Zettelsammlung` and so we don’t need to convert the
            # sammlung.
            return sammlung
        else:
            # When k==0, i.e. when no maximum number of zettel has
            # been set, for performance reasons `sammlung` is
            # initialized as an ordinary list and so at the end we
            # need to convert this list into a `Zettelsammlung`.
            return Zettelsammlung(sammlung)


if __name__ == '__main__':
    root = os.getenv('ZETTELSAMMLUNG_ROOT')
    sammlung = Zettelsammlung.collect_zettel(root, 50)
    print(len(sammlung))
    print(sammlung[:10])