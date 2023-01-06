import pygame

class TitleCard(pygame.sprite.Sprite):
    def __init__(self, content, x, y):
        super().__init__()
        self.font = pygame.font.Font('fonts/AGENCYB.ttf', 36)
        self.text = content
        self.xpos = x
        self.ypos = y
        self.transparent = False
        self.alpha = 255
        self.image = self.font.render(self.text, False, (99,155,255))
        self.rect = self.image.get_rect(midtop = (self.xpos, self.ypos))

    def update(self):
        self.image = self.font.render(self.text, False, (99,155,255))
        self.image.set_alpha(self.alpha)
        self.rect = self.image.get_rect(midtop = (self.xpos, self.ypos))

    def toggleTransparency(self):
        if self.transparent == True:
            print('toggle on')
            self.alpha = 255
            self.transparent = False
        elif self.transparent == False:
            print('toggle off')
            self.alpha = 0
            self.transparent = True