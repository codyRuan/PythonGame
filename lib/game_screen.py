import os
import sys
from easydict import EasyDict
import pygame
import socket
import json

from lib import Screen
from lib import player
from lib import maps


class GameScreen(Screen):
    def __init__(self, sock, screen):
        super().__init__()
        self.sock = sock
        self.screen = screen
        self.player_dict = {}

    def StopRequest(self):
        pass

    def ActionRequest(self, package: EasyDict):
        self.sock.send(json.dumps(package))
        self.sock.settimeout(2.0)
        res = self.sock.recv(4096)
        return EasyDict(json.loads(res))

    def Exec(self, opt: EasyDict):
        print('Game Screen')
        clock = pygame.time.Clock()
        framerate = 1.0 / opt.fps
        control = opt.control
        self.game_map = maps.get(opt.map.id)()
        for player_info in opt.players:
            p = player.get(player_info.id)()
            self.player_dict.append(p)

        while True:
            events = pygame.event.get()
            package = {}
            k = None
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        k = 0
                    elif event.key == pygame.K_RIGHT:
                        k = 1
                    elif event.key == pygame.K_DOWN:
                        k = 2
                    elif event.key == pygame.K_LEFT:
                        k = 3
                    elif event.key == pygame.K_SPACE:
                        k = 4
            package[f'player{control}'] = k
            res = self.ActionRequest(package)
            self.Update(res)
            pygame.display.flip()
            clock.tick(framerate)

    def InitializeGame():
        pass

    def Update(res):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.game_map.GetSurface(), (0, 0))
        for player_info in res.players:
            idx = player_info.id
            p = self.player_dict[idx]
            p.Update(player_info)
            self.screen.blit(p.GetSurface(), (p.y, p.x))
        return
