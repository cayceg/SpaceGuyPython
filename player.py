import pygame

from explosion import Explosion

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('sprites/player/Player.png').convert_alpha()
        self.rect = self.image.get_rect(center = (450,300))
        self.explode_sound = pygame.mixer.Sound('sounds/explode.wav')
        self.explode_sound.set_volume(0.1)
        pygame.mouse.set_pos(float(self.rect.centerx), float(self.rect.centery))

    def on_hit(self):
        self.explode_sound.play()
        self.kill()
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()