import cv2
import numpy as np
from abc import ABC
from zettelsortierung.DataTypes import BoundingBox
#from zettelsortierung.ImageAnnotation import BoundingBox


class OCRPreprocessor(ABC):
    def process_batch(self, image_batch: list[np.ndarray]) -> np.ndarray:
        pass

    @staticmethod
    def pad_boundingbox(boundingbox: BoundingBox, x_max: int, y_max: int, padding: int) -> BoundingBox:
        x, y, w, h = boundingbox
        x_new = max(0, x-padding)
        y_new = max(0, y-padding)
        w_new = min(w+2*padding, x_max-x_new)
        h_new = min(h+2*padding, y_max-y_new)
        return BoundingBox(x_new, y_new, w_new, h_new)
    
    @classmethod
    def pad_boundingboxes(cls, boundingboxes: list[BoundingBox], x_max, y_max, padding) -> list[BoundingBox]:
        return [cls.pad_boundingbox(boundingbox=bb, x_max=x_max, y_max=y_max, padding=padding) for bb in boundingboxes]

    @staticmethod
    def resize_im_patch(im_patch: np.ndarray, h_new: int) -> np.ndarray:
        h, w, c = im_patch.shape
        w_new = int(w * h_new / h)
        return cv2.resize(im_patch, (w_new, h_new))#, interpolation=cv2.INTER_AREA)

    @classmethod
    def resize_im_patches(cls, im_patches: list[np.ndarray], h_new: int) -> list[np.ndarray]:
        return [cls.resize_im_patch(im_patch=patch, h_new=h_new) for patch in im_patches]
    
    @staticmethod
    def cut_patch(image: np.ndarray, boundingbox: BoundingBox) -> np.ndarray:
        x, y, w, h = boundingbox
        return image[y:y+h, x:x+w]

    @staticmethod
    def cut_patches(image: np.ndarray, boundingboxes: list[BoundingBox]) -> list[np.ndarray]:
        return [image[y:y+h, x:x+w] for x, y, w, h in boundingboxes]

    @staticmethod
    def convert_im_patch_to_RGB(im_patch: np.ndarray) -> np.ndarray:
        return cv2.cvtColor(im_patch, cv2.COLOR_BGR2RGB)
        
    @staticmethod
    def convert_im_patches_to_RGB(im_patches: list[np.ndarray]) -> list[np.ndarray]:
        return [cv2.cvtColor(patch, cv2.COLOR_BGR2RGB) for patch in im_patches]


class PaddleOCRPreprocessor(OCRPreprocessor):
    ...