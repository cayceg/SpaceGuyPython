import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()

        player_rect = player.rect
        self.image = pygame.image.load('sprites/player/Bullet.png').convert_alpha()
        self.rect = self.image.get_rect(center = (player_rect.centerx, player_rect.centery - 20))
        self.speed = -10
        self.sound = pygame.mixer.Sound('sounds/player_shoot.wav')
        self.sound.set_volume(0.1)
        self.sound.play()
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom <= 0:
            self.destroy()

    def destroy(self):
        self.kill()