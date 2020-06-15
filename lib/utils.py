import pygame


class Button(object):
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y -
                                            2, self.width+4, self.height+4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y,
                                           self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                            self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


class Spark(pygame.sprite.Sprite):
    def __init__(self, scene):
        pygame.sprite.Sprite.__init__(self)
        self.main_scene = scene
        self.image = None
        self.rect = None
        self.frame = 0
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.images = []
        self.last_time = pygame.time.get_ticks()
        self.rate = 150

    def load(self, filename_prefix, begin_num, end_num,
                    filename_suffix):

        self.images = [
            pygame.image.load(filename_prefix + str(v) + filename_suffix)
            for v in range(begin_num, end_num + 1)
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.last_frame = end_num - 1

    def setpos(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def update(self, current_time, rate=60):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
            self.image = self.images[self.frame]

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > 0 and pos[0] < 0 + 800:
            if pos[1] > 365 and pos[1] < 365 + 235:
                return True

        return False


class Walk(pygame.sprite.Sprite):
    def __init__(self, scene):
        pygame.sprite.Sprite.__init__(self)
        self.main_scene = scene
        self.image = None
        self.rect = None
        self.frame = 0
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.images = []
        self.last_time = pygame.time.get_ticks()

    def load(self, filename_prefix, begin_num, end_num,
                    filename_suffix):

        self.images = [
            pygame.image.load(filename_prefix + str(v) + filename_suffix).convert()
            for v in range(begin_num, end_num + 1)
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.last_frame = end_num - 1

    def setpos(self,x,y):
        self.rect.x = x
        self.rect.y = y
    def update(self, current_time, rate=60):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
            self.image = self.images[self.frame]
            if self.rect.x < -50:
                self.rect.x = 820
            self.rect.x-=10