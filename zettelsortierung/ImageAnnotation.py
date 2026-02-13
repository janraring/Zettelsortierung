from dataclasses import dataclass, field
from typing import NamedTuple
import cv2


class BoundingBox(NamedTuple):
    x: int
    y: int
    w: int
    h: int


@dataclass
class AnnotatedImage:
    file_path: str
    annotated_text_regions: list[tuple[BoundingBox, str]] = field(default_factory=list)

    def add_text_region(self, region: BoundingBox, text: str):
        self.annotated_text_regions.append((region, text))
    
    def display_image(self):
        image = cv2.imread(self.file_path)
        for bounding_box, text in self.annotated_text_regions:
            x, y, w, h = bounding_box
            image = cv2.rectangle(img=image,
                pt1=(x, y),
                pt2=(x+w, y+h),
                color=(0, 0, 0),
                thickness=10
            )
            image = cv2.putText(img=image,
                text=text,
                org=(x, y-10),
                fontFace=0,
                fontScale=1.0,
                color=(0, 0, 0),
                thickness=2
            )

        resized_image = cv2.resize(image, (1500, 1000))

        cv2.imshow(winname="image", mat=resized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    example_file_path = 'data/raw/zettelsammlung/K23_Koo1-Kodde/1/01_Koo1/00186807_1#K23_1_01_Koo1.jpg'
    ai = AnnotatedImage(example_file_path)
    bb = BoundingBox(100, 200, 30, 40)
    text = 'nur ein test'
    ai.add_text_region(bb, text)
    ai.display_image()