'''
%
'''
import os
import sys
import socket
import argparse
from easydict import EasyDict
import pygame
pygame.init()
from lib import MainScreen
from lib import GameScreen


class Main(object):
    '''
    %
    '''

    def __init__(self):
        self.opt = self.Parse()
        self.clock = pygame.time.Clock()

    @staticmethod
    def Parse():
        '''%
        '''
        parg = argparse.ArgumentParser()
        parg.add_argument('-l', '--location',
                          default='localhost:8787', help='Location of server. Default: localhost:8000')
        opt = parg.parse_args()
        print(type(opt))
        opt.size = (720, 480)
        return opt

    def Main(self):
        screen = pygame.display.set_mode(self.opt.size)
        ip, port = self.opt.location.split(':')
        port = int(port)
        mainScreen = MainScreen(ip, port)
        game_started = False
        mainScreen.Exec(screen)


if __name__ == "__main__":
    Main().Main()
