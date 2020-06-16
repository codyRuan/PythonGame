import os
import sys
from easydict import EasyDict
import pygame
import socket
import ujson as json
from threading import Thread
from collections import deque
from lib import Screen
from lib import player
from lib import maps
from lib import bomb
from lib import watercol

from lib.end_screen import EndScreen

from lib import block


FPS = 80

class GameScreen(Screen):
    def __init__(self, sock, screen):
        super().__init__()
        self.sock = sock
        self.screen = screen
        self.player_dict = {}
        self.recv_queue = deque()
        self.recv_t = Thread(target=self.RecvThread)
        self.recv_t.start()
        self.group = pygame.sprite.Group()
        self.bomb_dict = {}
        self.watercol_dict = {}
        self.block_dict = {}

    def RecvThread(self):
        def parseStackedJson(s):
            print('Parsing...')
            stack = []
            ret = []
            start = 0
            for i, c in enumerate(s):
                if c == '{' or c == '[':
                    stack.append(c)
                elif c == '}' or c == ']':
                    stack.pop()
                if len(stack) == 0:
                    subs = s[start:i+1]
                    start = i + 1
                    ret.append(subs)
            return ret

        while True:
            recv_str = self.sock.recv(4096).decode('utf-8')
            print(f'RecvThread receives {recv_str} from server...')
            if recv_str == '':
                raise RuntimeError('Empty string error!')
            try:
                _ = json.loads(recv_str)
                recv_list = []
                recv_list.append(recv_str)
            except ValueError:
                recv_list = parseStackedJson(recv_str)
            for s in recv_list:
                self.recv_queue.append(s)

    def ActionSend(self, package: EasyDict):
        print(f'Sending {package} to server...')
        self.sock.send(json.dumps(package).encode())

    def Exec(self, opt: dict):
        print('Game Screen')
        pygame.mixer.music.load("./resources/BGM/game.mp3")
        
        pygame.mixer.music.play(-1,0.0)
        clock = pygame.time.Clock()
        fps = FPS
        control = opt.control
        if 'solidobject' in opt:
            blocks = opt.solidobject
        self.game_map = maps.get(opt.map.id)()
        for b in blocks:
            key = str(b[0]) + '-' + str(b[1])
            x = int(b[0])
            y = int(b[1])
            status = int(b[2])
            self.block_dict[key] = block.get(x, y, status)

        for player_info in opt.players:
            p = player.get(player_info.id)()
            p.SetPosition((player_info.x, player_info.y))
            self.player_dict[player_info.id] = p
        self.Update()
        while True:
            events = pygame.event.get()
            package = {}
            l = []
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
                            l.append(k)
                        Space_press = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                k = 3
                l.append(k)
            if keys[pygame.K_DOWN]:
                k = 2
                l.append(k)
            if keys[pygame.K_UP]:
                k = 0
                l.append(k)
            if keys[pygame.K_RIGHT]:
                k = 1
                l.append(k)
            for p in l:
                package[f'player{control}'] = p
                if p != -1:
                    self.ActionSend(package)
            if len(self.recv_queue):
                self.Update()
            self.group.update()
            self.group.draw(self.screen)
            pygame.display.flip()
            clock.tick(fps)

    def Update(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.game_map.GetSurface(), (0, 0))
        for key, value in self.block_dict.items():
            self.screen.blit(value.GetSurface(), (value.x, value.y))
        if len(self.recv_queue) > 0:
            recv_str = self.recv_queue.popleft()
            print('Recv str: ', recv_str)
            package = EasyDict(json.loads(recv_str))
            for data in package.data:
                if data.header == 'player_dead':
                    self.player_dict[data.idx].Dead()
                    screen1 = pygame.display.set_mode((800,600))
                    EndScreen(screen1).Exec(data.idx)
                elif data.header == 'player':
                    if 'position' in data:
                        self.player_dict[data.idx].SetPosition(data.position)
                    elif 'direction' in data:
                        self.player_dict[data.idx].SetDirection(data.direction)
                elif data.header == 'player_ability':
                    if 'position' in data:
                        key = str(data.position[0]) + '-' + str(data.position[1])
                        if self.block_dict.pop(key, None) == None:
                            raise RuntimeError(f'Item on {key} does not exist!')
                elif data.header == 'add_ball':
                    x, y = data.position
                    k = str(x)+'-'+str(y)
                    if k not in self.bomb_dict:
                        b = bomb.get(0, self.screen)
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
                    k = str(x)+'-'+str(y)
                    if k in self.bomb_dict:
                        print('Bomb removed')
                        self.group.remove(self.bomb_dict[k])
                        self.bomb_dict.pop(k, None)
                    if k not in self.watercol_dict:
                        h = watercol.get(0, x1, x2)
                        v = watercol.get(1, y1, y2)
                        self.watercol_dict[k] = (h, v)
                        self.group.add(h)
                        self.group.add(v)
                elif data.header == 'end_bomb':
                    x, y = data.position
                    k = str(x)+'-'+str(y)
                    if k in self.watercol_dict:
                        h, v = self.watercol_dict[k]
                        self.watercol_dict.pop(k, None)
                        self.group.remove(h)
                        self.group.remove(v)
        for k, p in self.player_dict.items():
            self.screen.blit(p.GetSurface(), (p.x, p.y))
        return
