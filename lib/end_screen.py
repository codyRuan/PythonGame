import pygame

from lib import Screen

class EndScreen(Screen):
    def __init__(self, screen):
        self.screen = screen
        self.text1 = None
        self.text2 = None

    def Draw(self, s):
        s = 1 if s == 1 else 2
        my_font = pygame.font.Font("./resources/font/Pixelony.ttf", 160)
        text_surface1 = my_font.render("Player{s}".format(s=s), True, (0,0,0), (255, 255, 255))
        text_surface2 = my_font.render("Win!", True, (0,0,0), (255, 255, 255))
        self.text1 = text_surface1
        self.text2 = text_surface2
    def Exec(self, s):
        pygame.mixer.init()
        pygame.mixer.music.load("./resources/BGM/start.mp3")
        pygame.mixer.music.play(-1,0.0)
        clock = pygame.time.Clock()
        self.Draw(s)
        while True:
            events = pygame.event.get()
            ticks = pygame.time.get_ticks()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.text1, (40, 100))
            self.screen.blit(self.text2, (250, 300))
            pygame.display.flip()
            clock.tick(50)