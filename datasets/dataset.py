from __future__ import print_function, division

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")
import os
import numpy as np
from torch.utils.data import Dataset
from PIL import Image


class ClassificationDataset(Dataset):

    def __init__(self, root, image_list, transform=None , is_grey = False):
        self.root = root
        self.image_list = image_list
        self.transform = transform
        self._read_txt_file()
        self.is_grey = is_grey

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        image = Image.open(self.img_paths[idx])
        if not self.is_grey:
            image = image.convert('RGB')
        else:
            image = image.convert('L')

        label = self.labels[idx][0]
        if self.transform:
            image = self.transform(image)
        return image, label

    def _read_txt_file(self):

        self.img_paths = []
        self.labels = []

        file_path = self.image_list
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                items = line.split(' ')
                lbls = [int(s) for s in items[1:]]
                self.img_paths.append(os.path.join(self.root,
                                                   items[0]))
                self.labels.append(np.array(lbls))

        self.labels = np.array(self.labels)
        print(len(self.labels))
        return


