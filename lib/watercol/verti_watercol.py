from lib.watercol.base_watercol import BaseWaterCol

class VertiWaterCol(BaseWaterCol):
    def __init__(self, start_position, end_position):
        self.width = 40
        self.height = end_position[1]*40 - start_position[1]*40 + 40
        super().__init__(self, start_position, self.width, self.height)