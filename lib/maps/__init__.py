from lib.maps.base import *
from lib.maps.map0 import Map0
from lib.maps.map1 import Map1

MAPS = [
    Map0,
    Map1
] 
def get(index):
    return MAPS[index]
