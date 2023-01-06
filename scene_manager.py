import pygame

class SceneManager():
    def load_scene(self, type):
        if type == 'title':
            print('in title')
        elif type == 'game':
            print('in game')
        elif type == 'hiscore':
            print('in hiscore')
        else:
            print(f'invalid scene: {type}')