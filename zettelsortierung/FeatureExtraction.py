from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Iterable
from itertools import chain

from multiprocessing import Pool
from functools import reduce
import operator
import cv2

from Zettelwerk import Zettel, Zettelsammlung
from ImageAnnotation import BoundingBox
from RegionDetection import OpenCVRegionDetector


#####################################################################


@dataclass(frozen=True, slots=True)
class DataPoint():
    zettel_id: str
    feature_id: int
    feature: Any


@dataclass(frozen=True)
class Probe():
    data_points: list[DataPoint] = field(default_factory=list)

    def __iter__(self):
        for data_point in self.data_points:
            yield data_point

    def add_data_point(self, data_point: DataPoint):
        self.data_points.append(data_point)
    
    def add_data_batch(self, data_points: list[DataPoint]):
        self.data_points.extend(data_points)

    def to_parquet(self):
        ...
    
    @staticmethod
    def from_parquet():
        ...


#####################################################################


class FeatureExtractor(ABC):
    @abstractmethod
    def extract(self, sammlung: Zettelsammlung) -> Probe:
        pass


class FeatureExtraction(ABC):
    def __init__(self,
                 extractor: FeatureExtractor,
                 sammlung: Zettelsammlung,
                 batch_size: int):
        self.extractor = extractor
        self.sammlung = sammlung
        self.batch_size = batch_size
        self.result = Probe()

    def batched(self) -> Iterable[Zettelsammlung]:
        teilsammlung = Zettelsammlung()
        for count, zettel in enumerate(self.sammlung, 1):
            teilsammlung.add(zettel)
            if count % self.batch_size == 0:
                yield teilsammlung
                teilsammlung.clear()

    @abstractmethod
    def run():
        pass


class FeatureProcessor(ABC):
    @abstractmethod
    def process(self, probe: Probe) -> Probe:
        pass

class FeatureProcessing(ABC):
    def __init__(self,
                 processor: FeatureProcessor,
                 probe: Probe,
                 batch_size: int):
        self.processor = processor
        self.probe = probe
        self.batch_size = batch_size
        self.result = Probe()

    def batched(self) -> Iterable[Probe]:
        teilprobe = Probe()
        for count, data_point in enumerate(self.probe, 1):
            teilprobe.add_data_point(data_point)
            if count % self.batch_size == 0:
                yield teilprobe
                teilprobe = Probe()
    
    @abstractmethod
    def run():
        pass

#####################################################################


class OpenCVBoundingBoxExtraction(FeatureExtraction):
    def __init__(self,
                 sammlung: Zettelsammlung,
                 batch_size: int,
                 parallel: bool=False):
        extractor = OpenCVBoundingBoxExtractor(parallel=parallel)
        super().__init__(extractor=extractor,
                         sammlung=sammlung,
                         batch_size=batch_size)

    def run(self):
        probes = [self.extractor.extract(teilsammlung)
                  for teilsammlung in self.batched()]
        for probe in probes:
            self.result.add_data_batch(probe.data_points)


class OpenCVBoundingBoxExtractor(FeatureExtractor):
    def __init__(self, parallel: bool=False):
        self.parallel = parallel
    
    def extract(self, sammlung: Zettelsammlung) -> Probe:
        if self.parallel:
            with Pool(12) as pool:
                data_point_lists = list(pool.imap_unordered(self.extraction_worker, sammlung))
        else:
            data_point_lists = [self.extraction_worker(zettel) for zettel in sammlung]
        flattend_list = list(chain.from_iterable(data_point_lists))
        return Probe(flattend_list)
    
    def extraction_worker(self, zettel: Zettelsammlung) -> list[DataPoint]:
        im_path = zettel.recto_file_path
        full_image = cv2.imread(im_path)
        boundingboxes = OpenCVRegionDetector.detect_regions(image=full_image)
        data_points = [DataPoint(zettel.id, feature_id, boundingbox)
                       for feature_id, boundingbox
                       in enumerate(boundingboxes)]
        return data_points


#####################################################################


class BoundingBoxPadding(FeatureProcessing):
    def __init__(self,
                 probe: Probe,
                 batch_size: int,
                 parallel: bool=False,
                 padding: int=10):
        processor = BoundingBoxPadder(parallel=parallel, padding=padding)
        super().__init__(processor=processor,
                         probe=probe,
                         batch_size=batch_size)
    
    def run(self):
        probes = [self.processor.process(teilprobe)
                  for teilprobe in self.batched()]
        for probe in probes:
            self.result.add_data_batch(probe.data_points)


class BoundingBoxPadder():
    def __init__(self, parallel: bool=False, padding: int=10):
        self.parallel = parallel
        self.padding = padding
    
    def process(self, probe: Probe) -> Probe:
        if self.parallel:
            with Pool(12) as pool:
                data_point_list = list(pool.imap_unordered(self.processing_worker, probe))
        else:
            data_point_list = [self.processing_worker(data_point) for data_point in probe]
        return Probe(data_point_list)
    
    def processing_worker(self, data_point: DataPoint) -> DataPoint:
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

            # Cout out patche
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



if __name__ == '__main__':
    sammlung = Zettelsammlung.from_parquet('./data/interim/test_path_collection.parquet', k=10)

    extraction = OpenCVBoundingBoxExtraction(sammlung=sammlung, batch_size=10, parallel=True)
    extraction.run()
    for data_point in extraction.result:
        print(data_point)
        break
    
    processing = BoundingBoxPadding(probe=extraction.result, batch_size=10, parallel=True, padding=10)
    processing.run()
    for data_point in processing.result:
        print(data_point)
        break
