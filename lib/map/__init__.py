from lib.map.base import *
from lib.map.map0 import Map0
from lib.map.map1 import Map1

MAPS = [
    Map0,
    Map1
] 
def getMap(index):
    return MAPS[index - 1]
