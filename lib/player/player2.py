from pathlib import Path

from lib.player.base_player import BasePlayer

class Player2(BasePlayer):
    def __init__(self):
        super.__init__()
        self.img_path = Path('resources/players/2')
        self.img = self.LoadImg()

