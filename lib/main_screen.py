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
from lib import Walk
from lib import Spark
from easydict import EasyDict


class MainScreen(Screen):
    def __init__(self, ip, port):
        super().__init__()
        self.main_group = pygame.sprite.Group()
        self.background = pygame.image.load('./resources/mainscreen/bg.png').convert_alpha()
        self.button = None
        #self.btn_start = Button((0, 255, 0), 0, 0, 720, 480, 'Start')
        self.server_ip = ip
        self.server_port = port

    def Draw(self, screen):
        self.button = Spark(screen)
        self.button.load('./resources/mainscreen/bt/',1,2,'.png')
        self.button.setpos(280,430)
        self.main_group.add(self.button)
        ball = Spark(screen)
        ball.load('./resources/bombs/bomb3/bomb',1,7,'.png')
        ball.setpos(490,85)
        self.main_group.add(ball)
        ball2 = Spark(screen)
        ball2.load('./resources/bombs/bomb2/bomb',1,8,'.png')
        ball2.setpos(560,230)
        self.main_group.add(ball2)
        man = Walk(screen)
        man.load('./resources/mainscreen/pic/', 1, 3, '.png')
        man.setpos(800,545)
        self.main_group.add(man)

    def Exec(self, screen):
        game_started = False
        sock = None
        clock = pygame.time.Clock()
        self.Draw(screen)
        while True:
            events = pygame.event.get()
            ticks = pygame.time.get_ticks()  
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(f'pos{pos}')
                    if self.button.isOver(pos):
                        print('Clicked!')
                        game_started = True
                        sock, res = self.StartRequest()
            pygame.display.flip()
            screen.blit(self.background, (0, 0))
            self.main_group.update(ticks,150)
            self.main_group.draw(screen)   
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

