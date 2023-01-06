import pygame

class InfoText(pygame.sprite.Sprite):
    def __init__(self, content, x, y):
        super().__init__()
        self.text = content
        self.xpos = x
        self.ypos = y
        self.font = pygame.font.Font('fonts/AGENCYB.ttf', 12)
        self.image = self.font.render(self.text, False, (60,60,60))
        self.rect = self.image.get_rect(midtop = (self.xpos, self.ypos))

    def update(self):
        self.image = self.font.render(self.text, False, (60,60,60))
        self.rect = self.image.get_rect(midtop = (self.xpos, self.ypos))