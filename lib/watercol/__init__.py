from lib.watercol.base_watercol import BaseWaterCol
from lib.watercol.hori_watercol import HoriWaterCol
from lib.watercol.verti_watercol import VertiWaterCol

WATERCOL = [
    HoriWaterCol,
    VertiWaterCol,
]
def get(index, sp, ep):
    return WATERCOL[index](sp,ep)