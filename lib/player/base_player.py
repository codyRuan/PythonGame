import pygame


class BasePlayer(object):
    def __init__(self):
        self.img_path = None
        self.img_size = (40, 40)
        self.x = None
        self.y = None
        self.status = 'ALIVE'
        self.direct = 2

    def LoadImg(self):
        #print(f'Loading player image from {self.img_path.resolve()}')
        img = pygame.image.load(str(self.img_path))
        img = pygame.transform.scale(img, self.img_size)
        return img

    # def SetPosition(self, x, y):
    #     self.x = x
    #     self.y = y


    def SetPosition(self, pos: list):
        self.x = pos[0]
        self.y = pos[1]

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    def GetSurface(self):
        return self.img
