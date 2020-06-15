import pygame

class BaseWaterCol(pygame.sprite.Sprite):
    def __init__(self, scene, initial_position, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.main_scene = scene
        self.image = pygame.Surface([width,height])
        self.image.fill((102,255,230))
        self.rect=self.image.get_rect()
        self.rect.topleft=(initial_position[0]*40, initial_position[1]*40)
    
    