from abc import ABC, abstractmethod
from enum import Enum
from typing import Iterable, overload, List, Iterator
from itertools import chain
from dataclasses import replace
from multiprocessing import Pool, cpu_count
import multiprocessing as mp
import cv2
import numpy as np
from tqdm import tqdm

from zettelsortierung import Sammlungen
from zettelsortierung.nn.models.mobilenet import MobileNetV3ModelSmall
from zettelsortierung.RegionDetection import RegionDetector
from zettelsortierung.DataTypes import (
    Collection,
    Zettelsammlung,
    DataPoint,
    DataPointBatch,
    Probe,
    BoundingBox,
    Scan,
    Classification,
    Label,
)

mp.set_start_method("spawn", force=True)
# cv2.setNumThreads(0)

#####################################################################
# Composition
#####################################################################


class Composition:
    def __init__(self, *transformations):
        self.sequence = transformations

    def __call__(self, collection: Collection) -> Iterable[Scan | DataPoint]:
        for app in self.sequence:
            collection = app(collection)
        return collection  # type: ignore


#####################################################################
# Application
#####################################################################


class Application(ABC):
    @abstractmethod
    def apply(self, collection: Collection) -> Probe | Iterable[DataPoint]:
        pass

    def __call__(self, collection: Collection) -> Probe | Iterable[DataPoint]:
        return self.apply(collection)


class SequentialApp(Application):
    def __init__(self, *transformations):
        self.sequence = Composition(*transformations)

    def apply(self, collection: Collection) -> Probe:
        return [self.sequence(item) for item in tqdm(collection)]  # type: ignore


class ParallelApp(Application):
    def __init__(self, *transformations):
        self.processes = cpu_count()
        self.sequence = Composition(*transformations)

    def apply(self, collection: Collection) -> Probe:
        with Pool(self.processes) as pool:
            return Probe(pool.imap_unordered(self.sequence, collection))  # type: ignore


class Print(Application):
    def apply(self, collection: Collection) -> Collection:
        print(collection)
        return collection


class Store(Application):
    def __init__(self, storage_container: Probe):
        self.storage_var: Probe = storage_container

    def apply(self, probe: Probe) -> Probe:
        self.storage_var.add_batch(probe)
        return probe


class ToDataBase(Application):
    def __init__(self, db_adder):
        self.db_adder = db_adder

    def apply(self, probe: Probe) -> Probe:
        self.db_adder(probe)
        return probe


class Sort(Application):
    def __init__(self, key):
        self.key = key

    def apply(self, collection: Collection) -> Probe:
        return Probe(sorted(collection, key=self.key))  # type: ignore


class Flatten(Application):
    @staticmethod
    @overload
    def apply(collection: list[list]) -> list: ...

    @staticmethod
    @overload
    def apply(collection: Probe) -> Probe: ...

    @staticmethod
    def apply(collection):
        if isinstance(collection, Probe):
            return Probe(chain.from_iterable(collection))  # type: ignore
        if isinstance(collection, List):
            return list(chain.from_iterable(collection))


class Batch(Application):
    def __init__(self, batch_size: int):
        self.batch_size = batch_size

    @overload
    def apply(self, collection: Zettelsammlung) -> Iterator[Zettelsammlung]: ...

    @overload
    def apply(self, collection: Probe) -> Iterator[Probe]: ...

    @overload
    def apply(self, collection: list) -> Iterator[list]: ...

    def apply(self, collection: Zettelsammlung | Probe | list) -> Iterator:
        collection_len = len(collection)
        subcollection = type(collection)()
        for count, scan in enumerate(collection, 1):
            if isinstance(subcollection, Zettelsammlung) and isinstance(scan, Zettel):
                subcollection.add(scan)
            if isinstance(subcollection, Probe) and isinstance(scan, DataPoint):
                subcollection.append(scan)
            if isinstance(subcollection, List):
                subcollection.append(scan)  # type: ignore
            if count % self.batch_size == 0 or count == collection_len:
                yield subcollection
                subcollection.clear()


#####################################################################
# Transformation
#####################################################################


class Transformation(ABC):
    @abstractmethod
    def transform(self, dp: Scan | DataPoint) -> DataPoint:
        pass

    def __call__(self, dp: Scan | DataPoint) -> DataPoint:
        return self.transform(dp)


class PrintDP(Transformation):
    def transform(self, dp: DataPoint) -> DataPoint:
        print(dp)
        return dp


class PatchDetect(Transformation):
    def __init__(self, detector: RegionDetector):
        self.detector = detector

    def transform(self, scan: Scan) -> list[DataPoint]:
        full_im = cv2.imread(scan.full_path)
        boundingboxes = self.detector.detect_regions(full_im)  # type: ignore
        data_points = [
            DataPoint(scan, feature_id, bbox)
            for feature_id, bbox in enumerate(boundingboxes)
        ]
        return data_points


class BoundingBoxPad(Transformation):
    def __init__(self, padding: int):
        self.padding = padding

    def transform(self, dp: DataPoint) -> DataPoint:
        y_max, x_max, d_max = dp.scan.shape
        x_old, y_old, w_old, h_old = dp.feature
        x = max(0, x_old - self.padding)
        y = max(0, y_old - self.padding)
        w = min(w_old + 2 * self.padding, x_max - x)
        h = min(h_old + 2 * self.padding, y_max - y)
        return replace(dp, feature=BoundingBox(x, y, w, h))


class CutOutPatch(Transformation):
    def transform(self, dp: DataPoint) -> DataPoint:
        image = cv2.imread(dp.scan.full_path)
        x, y, w, h = dp.feature
        patch = image[y : y + h, x : x + w]
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
        scan_batch = [dp.scan for dp in dp_batch]
        feature_id_batch = [dp.feature_id for dp in dp_batch]
        feature_batch = []
        w_max = max(dp.feature.shape[1] for dp in dp_batch)
        for dp in dp_batch:
            h, w, c = dp.feature.shape
            padded_patch = np.pad(
                dp.feature,
                ((0, 0), (0, w_max - w), (0, 0)),
                mode="constant",
                constant_values=0,
            )
            feature_batch.append(padded_patch)
        return DataPointBatch(scan_batch, feature_id_batch, np.stack(feature_batch))


class ResolveDPBatch(Transformation):
    def transform(self, dp_batch: DataPointBatch) -> list[DataPoint]:
        return [
            DataPoint(
                scan=dp_batch.scan_batch[i],
                feature_id=dp_batch.feature_id_batch[i],
                feature=dp_batch.feature_batch[i],
            )
            for i in range(len(dp_batch.scan_batch))
        ]


#####################################################################
# Model Predictions
#####################################################################

import torch
from torch.utils.data import DataLoader
from zettelsortierung import Zettel, Classification
from zettelsortierung.nn.datasets.pillist_dataset import PILListDataset
from zettelsortierung.nn.datasets.transforms import mobile_net_infer_transform


class PredictionModel(Transformation):
    def __init__(
        self,
        model: MobileNetV3ModelSmall,
        device: str,
        batch_size: int,
        classes: list[str],
        classifier: Enum,
    ):
        self.model = model
        self.device = device
        self.batch_size = batch_size
        self.classes = classes
        self.classifier = classifier

    def transform(self, paths) -> list[Classification]:
        dataset = PILListDataset(paths, mobile_net_infer_transform)
        loader = DataLoader(
            dataset, batch_size=self.batch_size, num_workers=12, pin_memory=True
        )

        path_batches = []
        logit_batches = []
        with torch.inference_mode():
            for path_batch, img_batch in tqdm(loader):
                path_batches.append(path_batch)
                img_batch = img_batch.xpu(non_blocking=True)
                img_batch.to(self.device)
                logits_batch = self.model(img_batch)
                logit_batches.append(logits_batch)

        probs = [torch.softmax(l, dim=1) for l in logit_batches]
        probs_flat = list(chain.from_iterable(probs))
        paths_flat = list(chain.from_iterable(path_batches))
        classifications = [
            Classification(
                zettel=Zettel(path),
                classifier=self.classifier,
                label=Label(
                    sammlung=Sammlungen[self.classes[int(prob.argmax().item())]],
                    confidence=prob.max().item(),
                ),
            )
            for path, prob in zip(paths_flat, probs_flat)
        ]
        return classifications
