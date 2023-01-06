import pygame
from button import ButtonFactory

from info_text import InfoText
from title_card import TitleCard

class IPopup(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.xpos = x
        self.ypos = y
        self.image = pygame.image.load('sprites/icons/Popup.png').convert_alpha()
        self.rect = self.image.get_rect(center = (self.xpos, self.ypos))

class HiscorePopup(IPopup):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.card = pygame.sprite.Sprite()
        self.card.image = self.image
        self.card.rect = self.rect
        self.title = InfoText('ENTER YOUR INITIALS', self.rect.centerx, self.rect.centery - 20)
        self.init1 = TitleCard('A', self.rect.centerx - 54, self.rect.centery)
        self.init2 = TitleCard('A', self.rect.centerx, self.rect.centery)
        self.init3 = TitleCard('A', self.rect.centerx + 54, self.rect.centery)
        self.contents = pygame.sprite.Group()
        self.contents.add(self.card)
        self.contents.add(self.title)
        self.contents.add(self.init1)
        self.contents.add(self.init2)
        self.contents.add(self.init3)
        self.target = self.init1

    def update(self):
        self.image = pygame.image.load('sprites/icons/Popup.png').convert_alpha()
        self.rect = self.image.get_rect(center = (self.xpos, self.ypos))
        self.contents.update()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.contents.draw(self.image)
    
class PausePopup(IPopup):
    def __init__(self, buttonGroup, x=0, y=0):
        super().__init__(x, y)
        self.buttonFactory = ButtonFactory()
        self.card = pygame.sprite.Sprite()
        self.card.image = self.image
        self.card.rect = self.rect
        self.title = InfoText('GAME PAUSED', self.rect.centerx, self.rect.centery - 20)
        self.backButton = self.buttonFactory.create_button('back', self.rect.centerx, self.rect.centery)
        self.quitButton = self.buttonFactory.create_button('quit', self.rect.centerx, self.rect.centery + 20)
        self.contents = pygame.sprite.Group()
        self.contents.add(self.card)
        self.contents.add(self.title)
        self.contents.add(self.backButton)
        buttonGroup.add(self.backButton)
        self.contents.add(self.quitButton)
        buttonGroup.add(self.quitButton)

    def update(self):
        self.image = pygame.image.load('sprites/icons/Popup.png').convert_alpha()
        self.rect = self.image.get_rect(center = (self.xpos, self.ypos))
        self.contents.update()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.contents.draw(self.image)