from pathlib import Path
import pygame
from easydict import EasyDict

from lib import block


class BaseMap(object):
    def __init__(self):
        self.map_path = None
        self.img_size = None
        self.block_list = []

    def LoadImg(self):
        print(f'Loading map image from {self.img_path.resolve()}')
        assert self.img_path.exists(), 'Path doesn\'t exist'
        img = pygame.image.load(str(self.img_path))
        img = pygame.transform.scale(img, self.img_size)
        return img

    def GetSurface(self):
        return self.img

    def AddBlock(self, x, y, index):
        element = block.get(x, y, index)
        self.block_list.append(element)
