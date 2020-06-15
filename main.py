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
                          default='localhost:8888', help='Location of server. Default: localhost:8888')
        opt = parg.parse_args()
        opt.size = (800, 600)
        return opt

    def Main(self):
        screen = pygame.display.set_mode(self.opt.size)
        ip, port = self.opt.location.split(':')
        port = int(port)
        mainScreen = MainScreen(ip, port)
        mainScreen.Exec(screen)


if __name__ == "__main__":
    Main().Main()
