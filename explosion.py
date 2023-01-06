import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.xpos = x
        self.ypos = y
        self.image = pygame.image.load('sprites/explode/Explode1.png').convert_alpha()
        self.rect = self.image.get_rect(center = (self.xpos, self.ypos))
        self.animation = ['sprites/explode/Explode1.png', \
                          'sprites/explode/Explode1.png', \
                          'sprites/explode/Explode1.png', \
                          'sprites/explode/Explode2.png', \
                          'sprites/explode/Explode2.png', \
                          'sprites/explode/Explode2.png', \
                          'sprites/explode/Explode3.png', \
                          'sprites/explode/Explode3.png', \
                          'sprites/explode/Explode3.png', \
                          'sprites/explode/Explode4.png', \
                          'sprites/explode/Explode4.png', \
                          'sprites/explode/Explode4.png', \
                          'sprites/explode/Explode5.png', \
                          'sprites/explode/Explode5.png', \
                          'sprites/explode/Explode5.png', \
                          'sprites/explode/Explode6.png', \
                          'sprites/explode/Explode6.png', \
                          'sprites/explode/Explode6.png']
        self.animIndex = 0
        self.points = 0
        self.hitPoints = 0

    def update(self):
        self.image = pygame.image.load(self.animation[self.animIndex]).convert_alpha()
        self.animIndex += 1
        if self.animIndex >= len(self.animation):
            self.destroy()

    def on_hit(self):
        pass

    def destroy(self):
        self.kill()