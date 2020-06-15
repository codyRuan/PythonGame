from lib.bomb.base_bomb import BaseBomb

class Bomb1(BaseBomb):
    def __init__(self, scene):
        super().__init__(scene)
        self.load_images('./resources/bombs/bomb1/bomb',1,4,'.png')
