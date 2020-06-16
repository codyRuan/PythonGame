import pygame


class BaseBlock(object):
    def __init__(self, x, y,  p='/path/to/img'):
        self.x = x
        self.y = y
        self.img_path = None
        self.img_size = (40, 40)
        self.img = self.LoadImage(p)

    def LoadImage(self, p):
        img = pygame.image.load(p)
        img = pygame.transform.scale(img, self.img_size)
        return img

    def GetSurface(self):
        return self.img

class SolidBlock(BaseBlock):
    def __init__(self, x, y):
        p = 'resources/items/wall.png'
        super().__init__(x, y, p)


class ShoesBlock(BaseBlock):
    def __init__(self, x, y):
        p = 'resources/items/shoes.png'
        super().__init__(x, y, p)


class AddBlock(BaseBlock):
    def __init__(self, x, y):
        p = 'resources/items/add.png'
        super().__init__(x, y, p)


class PowerBlock(BaseBlock):
    def __init__(self, x, y):
        p = 'resources/items/power.png'
        super().__init__(x, y, p)


class BreakableBlock(BaseBlock):
    def __init__(self, x, y):
        p = 'resources/items/breakable1.png'
        super().__init__(x, y, p)

BLOCKS = [
    SolidBlock,
    ShoesBlock,
    AddBlock,
    PowerBlock,
    None,
    BreakableBlock
]
def get(x, y, index):
    return BLOCKS[index](x, y)