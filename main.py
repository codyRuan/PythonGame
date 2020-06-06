import pygame
import argparse
import socket
from easydict import EasyDict


class Main(object):
    '''
    %
    '''

    def __init__(self):
        self.opt = self.Parse()

    @staticmethod
    def Parse():
        parg = argparse.ArgumentParser()
        parg.add_argument('-l', '--location',
                          default='localhost:8000', help='Location of server. Default: localhost:8000')
        parg = parg.parse_args()
        return parg

    def Main(self):
        pass


if __name__ == "__main__":
    Main().Main()
