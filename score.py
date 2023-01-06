import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.font = pygame.font.Font('fonts/AGENCYB.ttf', 24)
        self.image = self.font.render(f'{str(self.score).zfill(8)}', False, (255,255,255))
        self.rect = self.image.get_rect(topleft = (50, 34))

    def increment_score(self, score):
        self.score += score

    def update(self):
        self.image = self.font.render(f'{str(self.score).zfill(8)}', False, (255,255,255))
        self.rect = self.image.get_rect(topleft = (50, 34))