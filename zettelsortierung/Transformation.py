from abc import ABC, abstractmethod
from typing import Iterable
from itertools import chain
from multiprocessing import Pool, cpu_count
import multiprocessing as mp
from dataclasses import replace
import cv2
import numpy as np

from zettelsortierung.ImageAnnotation import BoundingBox
from zettelsortierung.RegionDetection import RegionDetector
from zettelsortierung.Datatypes import Collection, DataPoint, DataPointBatch, Probe, Zettel

mp.set_start_method("spawn", force=True)
#cv2.setNumThreads(0)

#####################################################################
# Composition
#####################################################################

class Composition:
    def __init__(self, *transformations):
        self.sequence = transformations
    
    def __call__(self, collection: Collection) -> Iterable[Zettel | DataPoint]:
        for app in self.sequence:
            collection = app(collection)
        return collection


#####################################################################
# Application
#####################################################################

class Application(ABC):
    @abstractmethod
    def apply(self, collection: Collection) -> Probe | Iterable[DataPoint]:
        pass

    def __call__(self, collection: Collection) -> Probe | Iterable[DataPoint]:
        return self.apply(collection)


# Brauche ich das überhaupt?
class Collect(Application):
    def apply(self, collection: Collection) -> Iterable[DataPoint]:
        return Probe(collection)


class DiagnosticsApp(Application):
    def apply(self, collection: Collection) -> Iterable[DataPoint]:
        print(collection)
        return collection


class SequentialApp(Application):
    def __init__(self, *transformations):
        self.sequence = Composition(*transformations)
    
    def apply(self, collection: Collection) -> Probe:
        return [self.sequence(item) for item in collection]


class ParallelApp(Application):
    def __init__(self, *transformations):
        self.processes = cpu_count()
        self.sequence = Composition(*transformations)
    
    def apply(self, collection: Collection) -> Probe:
        with Pool(self.processes) as pool:
            return Probe(pool.imap_unordered(self.sequence, collection))


class Flatten(Application):
    @staticmethod
    def apply(collection: Collection) -> Probe:
        return Probe(chain.from_iterable(collection))


class Batch(Application):
    def __init__(self, batch_size: int):
        self.batch_size = batch_size
    

class Batch(Application):
    def __init__(self, batch_size: int):
        self.batch_size = batch_size

    def apply(self, collection: Collection) -> Iterable[Collection]:
        collection_len = len(collection)
        subcollection = type(collection)()
        for count, zettel in enumerate(collection, 1):
            subcollection.add(zettel)
            if count % self.batch_size == 0 or count == collection_len:
                yield subcollection
                subcollection.clear()


class SortBoxWidth(Application):
    def apply(self, collection: Collection) -> Probe:
        return Probe(sorted(collection, key=lambda item: item.feature[2]))


class SortPatchWidth(Application):
    def apply(self, collection: Collection) -> Probe:
        return Probe(sorted(collection, key=lambda item: item.feature.shape[1]))


#####################################################################
# Transformation
#####################################################################

class Transformation(ABC):
    @abstractmethod
    def transform(self, dp: Zettel | DataPoint) -> DataPoint:
        pass

    def __call__(self, dp: Zettel | DataPoint) -> DataPoint:
        return self.transform(dp)


class DiagnosticsTransform(Transformation):
    def transform(self, dp: DataPoint) -> DataPoint:
        print(dp)
        return dp


class PatchDetect(Transformation):
    def __init__(self, detector: RegionDetector):
        self.detector = detector

    def transform(self, zettel: Zettel) -> list[DataPoint]:
        full_im = cv2.imread(zettel.recto.full_path)
        boundingboxes = self.detector.detect_regions(full_im)
        data_points = [DataPoint(zettel, feature_id, bbox)
                       for feature_id, bbox
                       in enumerate(boundingboxes)]
        return data_points


class BoundingBoxPad(Transformation):
    def __init__(self, padding: int):
        self.padding = padding
        
    def transform(self, dp: DataPoint) -> DataPoint:
        y_max, x_max, d_max = dp.zettel.recto.shape
        x_old, y_old, w_old, h_old = dp.feature
        x = max(0, x_old-self.padding)
        y = max(0, y_old-self.padding)
        w = min(w_old+2*self.padding, x_max-x)
        h = min(h_old+2*self.padding, y_max-y)
        return replace(dp, feature=BoundingBox(x, y, w, h))


class CutOutPatch(Transformation):
    def transform(self, dp: DataPoint) -> DataPoint:
        image = cv2.imread(dp.zettel.recto.full_path)
        x, y, w, h = dp.feature
        patch = image[y:y+h, x:x+w]
        return replace(dp, feature=patch)


class ResizePatch(Transformation):
    def transform(self, dp: DataPoint) -> DataPoint:
        h_old, w_old, c_old = dp.feature.shape
        h_new = 48
        w_new = int(w_old * h_new / h_old)
        patch = cv2.resize(dp.feature, (w_new, h_new))
        return replace(dp, feature=patch)


class BGR2RGB(Transformation):
    def transform(self, dp: DataPoint) -> DataPoint:
        converted = cv2.cvtColor(dp.feature, cv2.COLOR_BGR2RGB)
        return replace(dp, feature=converted)


class Stack(Transformation):
    def transform(self, dp_batch: list[DataPoint]) -> DataPointBatch:
        zettel_batch = [dp.zettel for dp in dp_batch]
        feature_id_batch = [dp.feature_id for dp in dp_batch]
        feature_batch = []
        w_max = max(dp.feature.shape[1] for dp in dp_batch)
        for dp in dp_batch:
            h, w, c = dp.feature.shape
            padded_patch = np.pad(dp.feature, ((0, 0), (0, w_max-w), (0, 0)), mode='constant', constant_values=0)
            feature_batch.append(padded_patch)
        return DataPointBatch(zettel_batch,
                              feature_id_batch,
                              np.stack(feature_batch))


class ResolveDPBatch(Transformation):
    def transform(self, dp_batch: DataPointBatch) -> list[DataPoint]:
        return [DataPoint(zettel=dp_batch.zettel_batch[i],
                               feature_id=dp_batch.feature_id_batch[i],
                               feature=dp_batch.feature_batch[i])
                for i in range(len(dp_batch.zettel_batch))]