from pathlib import Path

from lib.player.base_player import BasePlayer


class Player2(BasePlayer):
    def __init__(self):
        super().__init__()
        self.img_path = Path('resources/players/1/10.png').resolve()
        self.img = self.LoadImg()

    def SetBubbleImage(self):
        self.img_path = Path('resources/players/1/bubble.jpg').resolve()
        self.img = self.LoadImg()
    
    def SetDirection(self, d):
        if d == 3:
            self.img_path = Path('resources/players/1/1.png').resolve()
            self.img = self.LoadImg()
        if d == 2:
            self.img_path = Path('resources/players/1/10.png').resolve()
            self.img = self.LoadImg()
        if d == 0:
            self.img_path = Path('resources/players/1/7.png').resolve()
            self.img = self.LoadImg()
        if d == 1:
            self.img_path = Path('resources/players/1/4.png').resolve()
            self.img = self.LoadImg()
    def Dead(self):
        self.img_path = Path('resources/players/1/transparent.png').resolve()
        self.img = self.LoadImg()