from lib.bomb.base_bomb import BaseBomb

class Bomb2(BaseBomb):
    def __init__(self, scene):
        super().__init__(scene)
        self.load_images('./resources/bombs/bomb2/bomb',1,8,'.png')
