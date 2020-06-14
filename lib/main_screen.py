"""%
"""
import sys
import socket
import json
import pygame
from easydict import EasyDict

from lib import Screen
from lib import GameScreen
from lib import Button
from easydict import EasyDict


class MainScreen(Screen):
    def __init__(self, ip, port):
        super().__init__()
        self.btn_start = Button((0, 255, 0), 0, 0, 720, 480, 'Start')
        self.server_ip = ip
        self.server_port = port

    def Draw(self, screen):
        screen.fill((255, 255, 255))
        self.btn_start.draw(screen)

    def Exec(self, screen):
        game_started = False
        sock = None
        clock = pygame.time.Clock()
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
                        sock, res = self.StartRequest()
            pygame.display.flip()
            if game_started:
                GameScreen(sock, screen).Exec(EasyDict(json.loads(res)))
            clock.tick(50)

    def StartRequest(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.server_ip, self.server_port))
        package = {}
        package['request'] = 'START'
        s.send(json.dumps(package).encode())
        res = s.recv(4096).decode()
        print(f'Client receives {json.dumps(res, indent=4)}')
        return s, res

