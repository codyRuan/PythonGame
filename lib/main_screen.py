"""%
"""
import sys
import pygame

from lib import Screen
from lib import GameScreen
from lib import Button


class MainScreen(Screen):
    def __init__(self, opt):
        super().__init__(opt)
        self.btn_start = Button((0, 255, 0), 0, 0, 150, 150, 'Start')

    def Draw(self, screen):
        screen.fill((255, 255, 255))
        self.btn_start.draw(screen)

    def Exec(self, screen):
        gameScreen = GameScreen({})
        game_started = False
        while True:
            screen.fill((255, 255, 255))
            events = pygame.event.get()
            drew = self.Draw(screen)
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.btn_start.isOver(pos):
                        print('Clicked!')
                        game_started = True
            # screen.blit(drew, drew.get_rect())
            pygame.display.flip()
            if game_started:
                gameScreen.Exec(screen)
