import cv2
import numpy as np
from zettelsortierung.ImageAnnotation import BoundingBox
from abc import ABC, abstractmethod


class RegionDetector(ABC):
    @abstractmethod
    def detect_regions(image: np.ndarray) -> list[BoundingBox]:
        pass


class OpenCVRegionDetector(RegionDetector):
    @staticmethod
    def to_grayscale(image: np.ndarray) -> np.ndarray:
        if len(image.shape) == 3:
            return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image.copy()

    @staticmethod
    def normalize(image: np.ndarray) -> np.ndarray:
        return cv2.GaussianBlur(image, (25, 15), 0)
        
    @staticmethod
    def binarize(image: np.ndarray) -> np.ndarray:
        return cv2.adaptiveThreshold(
            image,
            maxValue=255,
            adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            thresholdType=cv2.THRESH_BINARY_INV,
            blockSize=45,
            C=10
        )

    @staticmethod
    def morph_rect_kernel():
        # This kernel joins handwriting strokes horizontally
        return cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (100, 20) # width >> height
        )

    @staticmethod
    def extract_morphology(image: np.ndarray, kernel):
        return cv2.morphologyEx(
            image,
            cv2.MORPH_CLOSE,
            kernel
        )

    @staticmethod
    def get_connected_components(grouped):
        return cv2.connectedComponentsWithStats(
            grouped,
            connectivity=8
        )

    @staticmethod
    def filter_geometrically(num_labels, stats, h_img: int, w_img: int) -> list[BoundingBox]:
        regions = []

        for i in range(1, num_labels):  # skip background
            x, y, w, h, area = stats[i]
            aspect_ratio = w / float(h)
            fill_ratio = area / float(w * h)

            # Typical handwritten 5-letter code heuristics
            if area < 1000:          # too small
                continue
            #if area > 20000:        # too big
            #    continue
            if aspect_ratio < 1.0:   # too narrow
                continue
            if aspect_ratio > 15.0:  # too wide
                continue
            if fill_ratio < 0.25:    # too sparse
                continue

            # Optional: restrict search area
            if x < w_img * 0.4 and y < h_img * 0.4:     # ignore upper left corner
                continue

            regions.append(BoundingBox(x, y, w, h))

        return regions

    @classmethod
    def detect_regions(cls, image: np.ndarray) -> list[BoundingBox]:
        """
        image: input page scan (BGR or grayscale)
        returns: list of bounding boxes [(x, y, w, h)]
        """
        # -------------------------
        # 1. Preprocessing
        # -------------------------
        gray = cls.to_grayscale(image)
        norm = cls.normalize(gray)

        # -------------------------
        # 2. Binarization
        # -------------------------
        binary = cls.binarize(norm)

        # -------------------------
        # 3. Morphological grouping
        # -------------------------
        kernel = cls.morph_rect_kernel()
        grouped = cls.extract_morphology(binary, kernel)

        # -------------------------
        # 4. Connected components
        # -------------------------
        num_labels, labels, stats, centroids = cls.get_connected_components(grouped)
        h_img, w_img = gray.shape

        # -------------------------
        # 5. Geometric filtering
        # -------------------------
        boxes = cls.filter_geometrically(num_labels, stats, h_img, w_img)

        return boxes


# Region methods
def resize_region(im_region: np.ndarray, h_new: int) -> np.ndarray:
    h, w, d = im_region.shape
    w_new = int(w * 48 / h)
    return cv2.resize(im_region, (w_new, h_new))  # TODO: try different methodes for interpolation
