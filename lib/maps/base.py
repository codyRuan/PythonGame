from pathlib import Path
import pygame


class BaseMap(object):
    def __init__(self):
        self.map_path = None
        self.img_size = None

    def LoadImg(self):
        print(f'Loading map image from {self.img_path}')
        img = pygame.image.load(self.img_path)
        img = pygame.transform.scale(img, self.img_size)
        return img
    
    def GetSurface(self):
        return self.img
