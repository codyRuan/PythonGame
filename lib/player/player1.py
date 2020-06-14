from pathlib import Path

from lib.player.base_player import BasePlayer


class Player1(BasePlayer):
    def __init__(self):
        super().__init__()
        self.img_path = Path('resources/players/1/image.png').resolve()
        self.img = self.LoadImg()
