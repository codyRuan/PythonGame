import pygame


class BaseMap(object):
    def __init__(self):
        self.size_block_x = None
        self.size_block_y = None
        self.map = None

    def PutBlock(self, x, y, tp='u'):
        """Put block on map

        Args:
            x (int)
            y (int)
            tp (str, optional): Type of block. Choices are 'u', 'b'. See note.md for more info. Defaults to 'u'.
        """
        self.map[y, x] = tp

    def BreakBlock(self, x, y):
        if self.map[y, x] == 'u':
            raise RuntimeError(f'Block at ({x}, {y}) is unbreakable!')
        else:
            self.map[y, x] = 'o'
