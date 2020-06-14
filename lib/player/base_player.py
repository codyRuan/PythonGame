import pygame


class BasePlayer(object):
    def __init__(self):
        self.img_path = None
        self.img_size = (40, 40)
        self.x = None
        self.y = None
        self.status = 'ALIVE'

    def LoadImg(self):
        print(f'Loading player image from {self.img_path}')
        img = pygame.image.load(self.img_path)
        img = pygame.transform.scale(img, self.img_size)
        return img

    def Update(self, info: EasyDict):
        self.x = info.x
        self.y = info.y
        self.status = info.status

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    def GetSurface():
        return self.img
