import pygame

class ButtonFactory():
    def __init__(self):
        self.type = ''
    
    def create_button(self, type, x, y):
        self.type = type
        if self.type == 'start':
            return StartButton(x, y)
        elif self.type == 'hiscore':
            return HiscoreButton(x, y)
        elif self.type == 'quit':
            return QuitButton(x, y)
        elif self.type == 'back':
            return BackButton(x, y)

class IButton(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0):
        super().__init__()
        self.image = pygame.image.load('sprites/icons/Menu Button.png').convert_alpha()
        self.rect = self.image.get_rect(center = (x,y))

    def on_down(self):
        print('button down')

    def on_up(self):
        print('button up')

    def on_over(self):
        print('button over')

class StartButton(IButton):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('sprites/icons/Start_Button.png').convert_alpha()
        self.rect = self.image.get_rect(center = (x,y))

    def on_down(self):
        down_event = pygame.event.Event(pygame.USEREVENT + 2)
        pygame.event.post(down_event)

    def on_up(self):
        self.image = pygame.image.load('sprites/icons/Start_Button.png').convert_alpha()

    def on_over(self):
        self.image = pygame.image.load('sprites/icons/Start_Button_Over.png').convert_alpha()

class QuitButton(IButton):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('sprites/icons/Quit_Button.png').convert_alpha()
        self.rect = self.image.get_rect(center = (x,y))

    def on_down(self):
        pygame.event.post(pygame.QUIT)

    def on_up(self):
        self.image = pygame.image.load('sprites/icons/Quit_Button.png').convert_alpha()

    def on_over(self):
        self.image = pygame.image.load('sprites/icons/Quit_Button_Over.png').convert_alpha()

class HiscoreButton(IButton):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('sprites/icons/Hiscores_Button.png').convert_alpha()
        self.rect = self.image.get_rect(center = (x,y))

    def on_down(self):
        down_event = pygame.event.Event(pygame.USEREVENT + 3)
        pygame.event.post(down_event)

    def on_up(self):
        self.image = pygame.image.load('sprites/icons/Hiscores_Button.png').convert_alpha()

    def on_over(self):
        self.image = pygame.image.load('sprites/icons/Hiscores_Button_Over.png').convert_alpha()

class BackButton(IButton):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('sprites/icons/Back_Button.png').convert_alpha()
        self.rect = self.image.get_rect(center = (x,y))

    def on_down(self):
        down_event = pygame.event.Event(pygame.USEREVENT + 1)
        pygame.event.post(down_event)

    def on_up(self):
        self.image = pygame.image.load('sprites/icons/Back_Button.png').convert_alpha()

    def on_over(self):
        self.image = pygame.image.load('sprites/icons/Back_Button_Over.png').convert_alpha()