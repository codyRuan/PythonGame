class BasePlayer(object):
    def __init__(self):
        self.img_path = None
        self.img_size = (40, 40)
        self.x = None
        self.y = None
        self.status = None

    def Update(self, info):
        self.x = info.x
        self.y = info.y
        self.status = info.status
