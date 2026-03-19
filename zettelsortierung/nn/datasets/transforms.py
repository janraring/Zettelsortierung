import torch
from torchvision import transforms
from PIL import ImageOps
from PIL.Image import Image

from zettelsortierung.nn.config import TrainingConfig


def pad_to_square(img, fill=(255, 255, 255)):
    w, h = img.size
    diff = abs(w - h)
    top = bottom = diff // 2
    bottom += diff % 2  # handle odd differences
    return ImageOps.expand(img, border=(0, top, 0, bottom), fill=fill)


mobile_net_train_transform = transforms.Compose(
    [
        transforms.Lambda(pad_to_square),
        transforms.Resize((TrainingConfig.input_size, TrainingConfig.input_size)),
        # Augmentation
        transforms.RandomRotation(degrees=3, fill=255),  # slight skew from scanning
        transforms.ColorJitter(
            brightness=0.2,  # uneven scan lighting
            contrast=0.2,  # faded or dark prints
            saturation=0.1,  # slight colour shift
        ),
        # To Tensor
        transforms.ToTensor(),  # scales pixels to [0.0, 1.0]
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],  # ImageNet mean
            std=[0.229, 0.224, 0.225],  # ImageNet std
        ),
    ]
)

mobile_net_infer_transform = transforms.Compose(
    [
        transforms.Lambda(pad_to_square),
        transforms.Resize((TrainingConfig.input_size, TrainingConfig.input_size)),
        # To Tensor
        transforms.ToTensor(),  # scales pixels to [0.0, 1.0]
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],  # ImageNet mean
            std=[0.229, 0.224, 0.225],  # ImageNet std
        ),
    ]
)
