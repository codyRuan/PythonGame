import numpy as np
import pygame
from pathlib import Path
from lib.maps import BaseMap


class Map0(BaseMap):
    def __init__(self):
        super.__init__()
        self.map_path = Path('resources/maps/0/back.png')
        self.img_size = (160, 160)
        self.img = self.LoadImg()
