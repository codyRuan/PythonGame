import pygame

class Bomb(pygame.sprite.Sprite):
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
 
    def load_images(self, filename_prefix, begin_num, end_num,
                    filename_suffix):
 
        self.images = [
            pygame.image.load(filename_prefix + str(v) + filename_suffix)
            for v in range(begin_num, end_num + 1)
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.last_frame = end_num -1
 

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y
 
    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time > self.last_time + self.rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
            self.image = self.images[self.frame]
            if self.rect.x < 0:
                self.rect.x = 580
            self.rect.x -= 8
        