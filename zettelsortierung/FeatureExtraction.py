from abc import ABC, abstractmethod
from typing import Iterable, Callable
from itertools import chain
from multiprocessing import Pool
import cv2
import numpy as np

from zettelsortierung.ImageAnnotation import BoundingBox
from zettelsortierung.RegionDetection import RegionDetector, OpenCVRegionDetector
from zettelsortierung.Datatypes import Collection, DataPoint, DataPointBatch, Probe, Zettel, Zettelsammlung
from zettelsortierung.OCR import OCRModel, PaddleOCR


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


class DiagnosticsApp(Application):
    def apply(self, collection: Collection) -> Probe:
        print(collection)
        return collection


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
    @staticmethod
    def apply(collection: Collection):
        return Probe(chain.from_iterable(collection))


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



#####################################################################
# Transformation
#####################################################################

class Transformation(ABC):
    @abstractmethod
    def transform(self, item: Collection) -> Probe:
        pass

    def __call__(self, item: Collection) -> Probe:
        return self.transform(item)


class DiagnosticsTransform(Transformation):
    def transform(self, dp: DataPoint) -> DataPoint:
        print(dp)
        return dp


class BoundingBoxPad(Transformation):
    def __init__(self, padding: int):
        self.padding = padding
        
    def transform(self, dp: DataPoint) -> DataPoint:
        x_max = 10000  # To be changed! TODO
        y_max = 10000  # To be changed! TODO
        x_old, y_old, w_old, h_old = dp.feature
        x = max(0, x_old-self.padding)
        y = max(0, y_old-self.padding)
        w = min(w_old+2*self.padding, x_max-x)
        h = min(h_old+2*self.padding, y_max-y)
        return DataPoint(zettel=dp.zettel,
                         feature_id=dp.feature_id,
                         feature=BoundingBox(x, y, w, h))


class PatchDetect(Transformation):
    def __init__(self, detector: RegionDetector):
        self.detector = detector

    def transform(self, zettel: Zettel) -> list[DataPoint]:
        full_im = cv2.imread(zettel.recto_file_path)
        boundingboxes = self.detector.detect_regions(full_im)
        data_points = [DataPoint(zettel, feature_id, bbox)
                       for feature_id, bbox
                       in enumerate(boundingboxes)]
        return data_points


class CutOutPatch(Transformation):
    def transform(self, dp: DataPoint) -> DataPoint:
        image = cv2.imread(dp.zettel.recto_file_path)
        x, y, w, h = dp.feature
        patch = image[y:y+h, x:x+w]
        return DataPoint(dp.zettel, dp.feature_id, patch)


class ResizePatch(Transformation):
    def transform(self, dp: DataPoint) -> DataPoint:
        h_old, w_old, c_old = dp.feature.shape
        h_new = 48
        w_new = int(w_old * h_new / h_old)
        patch = cv2.resize(dp.feature, (w_new, h_new))
        return DataPoint(dp.zettel, dp.feature_id, patch)


class BGR2RGB(Transformation):
    def transform(self, dp: DataPoint) -> DataPoint:
        converted = cv2.cvtColor(dp.feature, cv2.COLOR_BGR2RGB)
        return DataPoint(dp.zettel, dp.feature_id, converted)


class Stack(Transformation):
    def transform(self, dp_batch: list[DataPoint]) -> DataPointBatch:
        w_max = max(dp.feature.shape[1] for dp in dp_batch)
        zettel_batch = [dp.zettel for dp in dp_batch]
        feature_id_batch = [dp.feature_id for dp in dp_batch]
        feature_batch = []
        for dp in dp_batch:
            h, w, c = dp.feature.shape
            padded_patch = np.pad(dp.feature, ((0, 0), (0, w_max-w), (0, 0)), mode='constant', constant_values=0)
            feature_batch.append(padded_patch)
        return DataPointBatch(zettel_batch,
                              feature_id_batch,
                              np.stack(feature_batch))


class OCR(Transformation):
    def __init__(self, ocr_model: OCRModel):
        self.ocr_model = ocr_model

    def transform(self, dp_batch: DataPointBatch) -> list[DataPoint]:
        labels = self.ocr_model(dp_batch.feature_batch)
        return [DataPoint(dp_batch.zettel_batch[i],
                          dp_batch.feature_id_batch[i],
                          labels[i])
                for i in range(len(labels))]


#####################################################################
# Testing Area
#####################################################################

if __name__ == '__main__':
    sammlung = Zettelsammlung.from_parquet('./data/interim/test_path_collection.parquet', k=4)

    detector = OpenCVRegionDetector()

    pipeline = \
    Composition(
        Batch(100),
        SequentialApp(
            Composition(
                ParallelApp(10, PatchDetect(detector)),
                Flatten(),
                ParallelApp(10, BoundingBoxPad(10)),
                SortBoxWidth(),
                ParallelApp(10,
                    CutOutPatch(),
                    ResizePatch(),
                    BGR2RGB()
                ),
                Batch(4),
                ParallelApp(10, Stack()),
                SequentialApp(
                    OCR(PaddleOCR())
                ),
                Flatten()
            )
        ),
        Flatten()
    )

    result = pipeline(sammlung)
    print(result)