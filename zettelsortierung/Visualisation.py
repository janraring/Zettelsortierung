from zettelsortierung.DataTypes import DataPoint, DataPointBatch, BoundingBox, Scan
from zettelsortierung.DataModel import DataBase
import cv2

def vis_boundingbox(dp: DataPoint):
    image = cv2.imread(dp.zettel.recto_file_path)

    x, y, w, h = dp.feature
    image = cv2.rectangle(img=image,
        pt1=(x, y),
        pt2=(x+w, y+h),
        color=(0, 0, 0),
        thickness=10
    )

    image = cv2.resize(image, (1500, 1000))
    cv2.imshow(winname="region", mat=image)
    cv2.waitKey(delay=0)
    cv2.destroyAllWindows()

def vis_patch(dp: DataPoint):
    cv2.imshow(winname="region", mat=dp.feature)
    cv2.waitKey(delay=0)
    cv2.destroyAllWindows()

def vis_image(im):
    cv2.imshow(winname="region", mat=im)
    cv2.waitKey(delay=0)
    cv2.destroyAllWindows()

def vis_image_path(im_path):
    print(im_path)
    im = cv2.imread(im_path)
    cv2.imshow(winname="region", mat=im)
    cv2.waitKey(delay=0)
    cv2.destroyAllWindows()

def vis_anno(dp: DataPoint):
    image = cv2.imread(dp.zettel.recto_file_path)
    image = cv2.resize(image, (1500, 1000))
    cv2.imshow(winname=dp.feature, mat=image)
    cv2.waitKey(delay=0)
    cv2.destroyAllWindows()

def vis_batch(dpb: DataPointBatch):
    for i in range(len(dpb.feature_batch)):
        vis_image(dpb.feature_batch[i])

def vis_boxes_labels(scan: Scan, boxes: list[BoundingBox], texts: list[str]):
    image = cv2.imread(scan.full_path)
    for box, text in zip(boxes, texts):
        x, y, w, h = box
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

    cv2.imshow(winname=scan.id, mat=resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

db = DataBase()

def vis_scan(scan_id: str):
    path = db.get_full_path(scan_id)[0]
    image = cv2.imread(path)
    image = cv2.resize(image, (1500, 1000))
    cv2.imshow(winname=scan_id, mat=image)
    cv2.waitKey(delay=0)
    cv2.destroyAllWindows()