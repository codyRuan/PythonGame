import os
import sys
import pygame
from pathlib import Path

from lib import Screen


class GameScreen(Screen):
    def __init__(self, opt):
        super().__init__(opt)
        
    def Draw(self):
        pass

    def Exec(self, screen):
        print('Game Screen')
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
            screen.fill((0, 0, 0))
            pygame.display.flip()