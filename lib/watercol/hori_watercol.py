from lib.watercol.base_watercol import BaseWaterCol

class HoriWaterCol(BaseWaterCol):
    def __init__(self, start_position, end_position):
        self.width = end_position[0]*40 - start_position[0]*40 + 40
        self.height = 40
        super().__init__(self, start_position, self.width, self.height)