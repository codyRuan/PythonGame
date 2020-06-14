import os
import sys
from easydict import EasyDict
import pygame
import socket
import ujson as json
from threading import Thread

from lib import Screen
from lib import player
from lib import maps

FPS = 30.0


class GameScreen(Screen):
    def __init__(self, sock, screen):
        super().__init__()
        self.sock = sock
        self.screen = screen
        self.player_dict = {}
        self.recv_str = ''
        self.recv_t = Thread(target=self.recvThread)
        self.recv_t.start()

    def recvThread(self):
        while True:
            self.recv_str = self.sock.recv(4096).decode()
            print(f'recvThread receives {self.recv_str} from server...')

    def ActionSend(self, package: EasyDict):
        print(f'Sending {package} to server...')
        self.sock.send(json.dumps(package).encode())

    def Exec(self, opt: dict):
        print('Game Screen')
        clock = pygame.time.Clock()
        fps = FPS
        framerate = 1.0 / fps
        control = opt.control
        self.game_map = maps.get(opt.map.id)()
        for player_info in opt.players:
            p = player.get(player_info.id)()
            p.SetPosition((player_info.x, player_info.y))
            self.player_dict[player_info.id] = p
        self.Update()
        while True:
            events = pygame.event.get()
            package = {}
            k = -1
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(f'Key {event.key} is pressed')
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
            if k != -1:
                self.ActionSend(package)
            if self.recv_str != '':
                self.Update()
            pygame.display.flip()
            clock.tick(fps)

    def InitializeGame():
        pass

    def Update(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.game_map.GetSurface(), (0, 0))
        if self.recv_str != '':
            package = EasyDict(json.loads(self.recv_str))
            for data in package.data:
                if data.header == 'player_dead':
                    self.player_dict[data.idx] = 'DEAD'
                elif data.header == 'player':
                    if 'position' in data:
                        self.player_dict[data.idx].SetPosition(data.position)
                    elif 'direction' in data:
                        self.player_dict[data.idx].SetDirection(data.direction)
                elif data.header == 'add_ball':
                    print('balls')
                elif data.header == 'water_area':
                    print('w')
                elif data.header == 'end_bomb':
                    print('.')
        for k, p in self.player_dict.items():
            self.screen.blit(p.GetSurface(), (p.x, p.y))
        return
