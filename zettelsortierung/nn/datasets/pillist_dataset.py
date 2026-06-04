from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms
from zettelsortierung.DataTypes import Zettel


class PILListDataset(Dataset):
    def __init__(self, zettelpaths: list[str], transform=None):
        self.zettelpaths = zettelpaths
        self.transform = transform or transforms.ToTensor()

    def __len__(self):
        return len(self.zettelpaths)

    def __getitem__(self, idx):
        path = self.zettelpaths[idx]
        img = Image.open(path)
        transformed = self.transform(img)
        return path, transformed
