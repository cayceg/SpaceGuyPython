import pygame

class Life(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0):
        super().__init__()
        self.image = pygame.image.load('sprites/icons/1Up.png').convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))

class LivesContainer(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def add(self, *sprites) -> None:
        super().add(*sprites)
        self.reposition_lives()

    def remove(self, *sprites) -> None:
        super().remove(*sprites)
        self.reposition_lives()

    def reposition_lives(self):
        count = 0
        for life in self:
            life.rect.y = 350
            life.rect.x = 50 + (count * 20)
            count += 1