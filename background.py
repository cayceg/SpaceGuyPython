import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load('sprites/bg/GAME_BG.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (x,y))
        self.speed = 2
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 0:
            group = self.groups()[0]
            if len(group) <= 2:
                group.add(Background(0, -400))
        if self.rect.y > 400:
            self.kill()