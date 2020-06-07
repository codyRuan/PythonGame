import numpy as np
import pygame
from pathlib import Path
from lib.map import BaseMap


class Map0(BaseMap):
    def __init__(self):
        super.__init__()
        self.config()

    def Config():
        res_path = Path.cwd().parent.parent.parent / 'resources' / 'map1'
        print(f'Resource path: {res_path.resolve()}')
        self.background_path = res_path / 'back.png'
        self.block_path = res_path / 'block.png'
        try:
            self.background_img = pygame.image.load(str(self.background_path))
            self.block_img = pygame.image.load(str(self.block_path))
        except pygame.error as msg:
            print('Cannot load image:', name)
            raise SystemExit(message)
        self.background_img = self.background_img.convert()
        self.block_img = self.block_img.convert()
        self.size_block_x = 4
        self.size_block_y = 4
        self.map = np.ndarray(
            (self.size_block_y, self.size_block_x), dtype=np.char).fill('o')


    def Put(self, x, y):
        pass
