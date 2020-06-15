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
from lib import bomb
from lib import watercol

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
        self.group = pygame.sprite.Group()
        self.bomb_dict = {}
        self.watercol_dict = {}

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
                    if event.key == pygame.K_SPACE:
                        Space_press = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        if Space_press == True:
                            k = 4
                        Space_press = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                k = 3
            if keys[pygame.K_DOWN]:
                k = 2
            if keys[pygame.K_UP]:
                k = 0
            if keys[pygame.K_RIGHT]:
                k = 1
            package[f'player{control}'] = k
            if k != -1:
                self.ActionSend(package)
            if self.recv_str != '':
                self.Update()
            self.group.update()
            self.group.draw(self.screen)
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
                    x, y = data.position
                    k = str(x)+str(y)
                    if k not in self.bomb_dict:
                        b = bomb.get(0,self.screen)
                        b.set_pos(data.position[0]*40, data.position[1]*40)
                        self.bomb_dict[k] = b
                        self.group.add(b)
                elif data.header == 'water_area':
                    x1, y1, x2, y2 = data.area
                    poses = data.player_to_bubble_pos
                    idxes = data.player_to_bubble_idx
                    for idx in idxes:
                        self.player_dict[idx].SetBubbleImage()
                    #print(f'x1:{x1}, x2:{x2}, y1:{y1}, y2:{y2}')
                    x, y = data.position
                    k = str(x)+str(y)
                    if k in self.bomb_dict:
                        self.group.remove(self.bomb_dict[k])
                        self.bomb_dict.pop(k,None)
                    if k not in self.watercol_dict:
                        h = watercol.get(0,x1,x2)
                        v = watercol.get(1,y1,y2)
                        self.watercol_dict[k] = (h,v)
                        self.group.add(h)
                        self.group.add(v)
                elif data.header == 'end_bomb':
                    x, y = data.position
                    k = str(x)+str(y)
                    if k in self.watercol_dict:
                        h, v = self.watercol_dict[k]
                        self.watercol_dict.pop(k,None)
                        self.group.remove(h)
                        self.group.remove(v)
        for k, p in self.player_dict.items():
            self.screen.blit(p.GetSurface(), (p.x, p.y))
        return
