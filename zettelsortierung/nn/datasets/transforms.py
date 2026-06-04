from torchvision import transforms
from PIL import ImageOps

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

mobile_net_aggr_transform = transforms.Compose(
    [
        transforms.Lambda(pad_to_square),
        transforms.Resize((TrainingConfig.input_size, TrainingConfig.input_size)),
        # Geometry
        transforms.RandomRotation(degrees=5, fill=255),
        transforms.RandomPerspective(distortion_scale=0.15, p=0.4, fill=255),
        transforms.RandomAffine(
            degrees=0, translate=(0.05, 0.05), fill=255
        ),  # slight mis-centering
        # Photometric
        transforms.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.15, hue=0.02),
        transforms.RandomGrayscale(
            p=0.1
        ),  # some scans are effectively greyscale anyway
        transforms.GaussianBlur(kernel_size=3, sigma=(0.1, 1.5)),  # scanner softness
        # To Tensor
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        # Tensor-space augmentations
        transforms.RandomErasing(
            p=0.25, scale=(0.02, 0.08), value=1
        ),  # simulate scan artifacts / stamps
    ]
)
