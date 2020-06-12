import os
import sys
from easydict import EasyDict
import pygame
import socket
import json

from lib import Screen
from lib.map import Map0


class GameScreen(Screen):
    def __init__(self, sock, screen):
        super().__init__()
        self.sock = sock
        self.screen = screen

    def StopRequest(self):
        pass

    def ActionRequest(self, package):
        self.sock.send(json.dumps(package))
        self.sock.settimeout(2.0)
        res = self.sock.recv(4096)
        return EasyDict(json.loads(res))

    def Exec(self, opt):
        print('Game Screen')
        clock = pygame.time.Clock()
        framerate = 1.0 / opt.fps
        map_id = opt.map.id
        control = opt.control
        players = opt.players

        while True:
            events = pygame.event.get()
            package = {}
            k = None
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        k = 1
                    elif event.key == pygame.K_RIGHT:
                        k = 2
                    elif event.key == pygame.K_DOWN:
                        k = 3
                    elif event.key == pygame.K_LEFT:
                        k = 4
                    elif event.key == pygame.K_SPACE:
                        k = 5
            package[f'player{control}'] = k
            res = self.ActionRequest(package)
            self.Update(res)
            pygame.display.flip()
            clock.tick(framerate)

    def InitializeGame():

    def Update(res):
        self.screen.fill((0, 0, 0))
        return
