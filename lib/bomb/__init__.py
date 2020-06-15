from lib.bomb.base_bomb import BaseBomb
from lib.bomb.bomb1 import Bomb1
from lib.bomb.bomb2 import Bomb2
BOMBS = [
    Bomb1,
    Bomb2,
]
def get(index, s):
    return BOMBS[index](s)