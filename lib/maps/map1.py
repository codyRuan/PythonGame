import numpy as np
import pygame
from pathlib import Path
from lib.maps import BaseMap


class Map1(BaseMap):
    def __init__(self):
        super().__init__()
        self.img_path = Path('resources/maps/1/back.png').resolve()
        self.img_size = (320, 320)
        self.img = self.LoadImg()
