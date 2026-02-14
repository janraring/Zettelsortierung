from abc import ABC, abstractmethod
from typing import Iterable, Callable
from itertools import chain
from multiprocessing import Pool
import cv2

from ImageAnnotation import BoundingBox
from RegionDetection import RegionDetector, OpenCVRegionDetector
from Datatypes import Collection, DataPoint, Probe, Zettel, Zettelsammlung


#####################################################################
# Reference
#####################################################################

def extraction_worker_old(self, zettel):
    im_path = zettel.recto_file_path
    full_image = cv2.imread(im_path)
    y_max, x_max, c_max = full_image.shape

    unpadded_boundingboxes = self.region_detector.detect_regions(image=full_image)
    patch_dict = {}

    for unpadded_boundingbox in unpadded_boundingboxes:
        # Pad boundingbox
        padding = 10
        x_old, y_old, w_old, h_old = unpadded_boundingbox
        x = max(0, x_old-padding)
        y = max(0, y_old-padding)
        w = min(w_old+2*padding, x_max-x)
        h = min(h_old+2*padding, y_max-y)
        boundingbox = BoundingBox(x, y, w, h)


        # Cut out patche
        unresized_im_patch = full_image[y:y+h, x:x+w]

        # Resize patch
        h_new = 48
        w_new = int(w * h_new / h)
        unconverted_im_patch = cv2.resize(unresized_im_patch, (w_new, h_new))

        # Convert BGR to RGB
        im_patch = cv2.cvtColor(unconverted_im_patch, cv2.COLOR_BGR2RGB)
        
        # Store result
        patch_dict[(im_path, boundingbox)] = im_patch

    return patch_dict






#####################################################################
# Composition
#####################################################################

class Composition:
    def __init__(self, *transformations):
        self.sequence = transformations
    
    def __call__(self, collection: Collection):
        for app in self.sequence:
            collection = app(collection)
        return collection


#####################################################################
# Application
#####################################################################

class Application(ABC):
    @abstractmethod
    def apply(self, item: Collection) -> Probe:
        pass

    def __call__(self, item: Collection) -> Probe:
        return self.apply(item)


class SequentialApp(Application):
    def __init__(self, *transformations):
        self.sequence = Composition(*transformations)
    
    def apply(self, collection: Collection) -> Probe:
        return Probe([self.sequence(item) for item in collection])


class ParallelApp(Application):
    def __init__(self, processes: int, *transformations):
        self.processes = processes
        self.sequence = Composition(*transformations)
    
    def apply(self, collection: Collection) -> Probe:
        with Pool(self.processes) as pool:
            return Probe(pool.imap_unordered(self.sequence, collection))


class Flatten(Application):
    def apply(self, collection: Collection):
        return list(chain.from_iterable(collection))


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


class Sort(Application):
    ...


#####################################################################
# Transformation
#####################################################################

class Transformation(ABC):
    @abstractmethod
    def transform(self, item: Collection) -> Probe:
        pass

    def __call__(self, item: Collection) -> Probe:
        return self.transform(item)


class BoundingBoxPad(Transformation):
    def __init__(self, padding: int):
        self.padding = padding
        
    def transform(self, data_point: DataPoint) -> DataPoint:
        x_max = 10000  # To be changed! TODO
        y_max = 10000  # To be changed! TODO
        x_old, y_old, w_old, h_old = data_point.feature
        x = max(0, x_old-self.padding)
        y = max(0, y_old-self.padding)
        w = min(w_old+2*self.padding, x_max-x)
        h = min(h_old+2*self.padding, y_max-y)
        return DataPoint(zettel_id=data_point.zettel_id,
                         feature_id=data_point.feature_id,
                         feature=BoundingBox(x, y, w, h))


class PatchDetect(Transformation):
    def __init__(self, detector: RegionDetector):
        self.detector = detector

    def transform(self, zettel: Zettel) -> list[DataPoint]:
        full_im = cv2.imread(zettel.recto_file_path)
        boundingboxes = self.detector.detect_regions(full_im)
        data_points = [DataPoint(zettel.id, feature_id, bbox)
                       for feature_id, bbox
                       in enumerate(boundingboxes)]
        return data_points




#####################################################################
# Testing Area
#####################################################################

if __name__ == '__main__':
    sammlung = Zettelsammlung.from_parquet('./data/interim/test_path_collection.parquet', k=3)

    detector = OpenCVRegionDetector()

    pipeline = Composition(
        ParallelApp(10, PatchDetect(detector)),
        Flatten(),
        ParallelApp(10, BoundingBoxPad(10))
    )

    padded = pipeline(sammlung)
    for datum in padded:
        print(datum)