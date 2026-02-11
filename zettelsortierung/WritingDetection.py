import cv2
import numpy as np
from zettelsortierung.Zettelwerk import Zettel

def to_grayscale(image: np.ndarray) -> np.ndarray:
    if len(image.shape) == 3:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image.copy()

def normalize(image: np.ndarray) -> np.ndarray:
    return cv2.GaussianBlur(image, (25, 15), 0)
    
def binarize(image: np.ndarray) -> np.ndarray:
    return cv2.adaptiveThreshold(
        image,
        maxValue=255,
        adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        thresholdType=cv2.THRESH_BINARY_INV,
        blockSize=45,
        C=10
    )

def morph_rect_kernel():
    # This kernel joins handwriting strokes horizontally
    return cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (100, 20) # width >> height
    )

def extract_morphology(image, kernel):
    return cv2.morphologyEx(
        image,
        cv2.MORPH_CLOSE,
        kernel
    )

def get_connected_components(grouped):
    return cv2.connectedComponentsWithStats(
        grouped,
        connectivity=8
    )

def filter_geometrically(num_labels, stats, h_img: int, w_img: int) -> list[tuple]:
    boxes = []

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

        boxes.append((x, y, w, h))

    print(type(boxes[0]))
    return boxes

def sort_boxes(boxes: list[tuple]) -> list[tuple]:
    return sorted(
        boxes,
        key=lambda b: b[2] * b[3],
        reverse=False
        #reverse=True
    )


def detect_code_regions(image: np.ndarray) -> list[tuple]:
    """
    image: input page scan (BGR or grayscale)
    returns: list of bounding boxes [(x, y, w, h)]
    """
    # -------------------------
    # 1. Preprocessing
    # -------------------------
    gray = to_grayscale(image)
    norm = normalize(gray)

    # -------------------------
    # 2. Binarization
    # -------------------------
    binary = binarize(norm)

    # -------------------------
    # 3. Morphological grouping
    # -------------------------
    kernel = morph_rect_kernel()
    grouped = extract_morphology(binary, kernel)

    # -------------------------
    # 4. Connected components
    # -------------------------
    num_labels, labels, stats, centroids = get_connected_components(grouped)
    h_img, w_img = gray.shape

    # -------------------------
    # 5. Geometric filtering
    # -------------------------
    boxes = filter_geometrically(num_labels, stats, h_img, w_img)

    # Sort candidates by likelihood (example: area descending)
    boxes = sort_boxes(boxes)

    # Return top N candidates
    return boxes#[:5]

def display_boxes(image: np.ndarray, boxes: list[tuple]):
    for index, box in enumerate(boxes):
        x, y, w, h = box
        aspect_ratio = w / float(h)

        stats = f'Box {index}: {aspect_ratio:.2f}'

        image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 0), 10)
        image = cv2.putText(image, stats, (x-60, y-10), 0, 1.0, (0, 0, 0), 2)
    image = cv2.resize(image, (1500, 1000))
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class WritingDetector:
    pass

if __name__ == '__main__':
    pass
