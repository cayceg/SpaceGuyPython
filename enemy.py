import pygame
import math

from bullet import Bullet
from explosion import Explosion

class EnemyFactory():
    def __init__(self):
        self.type = ''

    def create_enemy(self, type, x, y):
        self.type = type
        if self.type == 'basic':
            return BasicEnemy(x, y)
        if self.type == 'shooter':
            return ShooterEnemy(x, y)
        if self.type == 'swerve':
            return SwerveEnemy(x, y)

class IEnemy(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0):
        super().__init__()
        self.image = pygame.image.load('sprites/enemy/Enemy.png').convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))
        self.explode_sound = pygame.mixer.Sound('sounds/explode.wav')
        self.explode_sound.set_volume(0.1)
        self.speed = 3
        self.direction = 90.0
        self.points = 100
        self.hitPoints = 2
    
    def on_hit(self):
        self.hitPoints -= 1
        if self.hitPoints <= 0:
            self.explode_sound.play()
            self.destroy()
    
    def update(self):
        movement = self.calculate_movement(self.speed)
        self.rect.x += movement[0]
        self.rect.y += movement[1]

        if self.is_out_of_bounds():
            self.destroy()

    def destroy(self):
        enemy_group = self.groups()[0]
        enemy_group.add(Explosion(self.rect.centerx, self.rect.centery))
        self.kill()

    def calculate_movement(self, speed):
        x = 0
        y = speed
        movement = (x, y)
        return movement

    def is_out_of_bounds(self):
        if self.rect.x >= 1200:
            return True
        elif self.rect.x <= -300:
            return True
        elif self.rect.y >= 700:
            return True
        elif self.rect.y <= -300:
            return True
        else:
            return False

class BasicEnemy(IEnemy):
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)

class SwerveEnemy(IEnemy):
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)
        self.points = 200

    def calculate_movement(self, speed):
        phase = pygame.time.get_ticks()
        frequency = 6
        magnitude = 5
        x = magnitude * math.sin(math.radians(phase / frequency))
        y = speed
        movement = (x, y)
        return movement

class ShooterEnemy(IEnemy):
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)
        self.points = 150
        self.volley_delay = 300
        self.volleys = 3
        self.volley_count = 0
        self.last_volley = pygame.time.get_ticks()
        self.delta_time = 0
    
    def update(self):
        self.delta_time =  pygame.time.get_ticks() - self.last_volley
        movement = self.calculate_movement(self.speed)
        self.rect.x += movement[0]
        self.rect.y += movement[1]

        if self.volley_count < self.volleys:
            if self.delta_time >= self.volley_delay:
                enemy_group = self.groups()[0]
                enemy_group.add(BulletEnemy(self.rect.centerx, self.rect.centery))
                self.last_volley = pygame.time.get_ticks()
                self.volley_count += 1    

        if self.is_out_of_bounds():
            self.destroy()

class BulletEnemy(IEnemy):
    def __init__(self, x = 0, y = 0, dir = 90.0):
        super().__init__()
        self.image = pygame.image.load('sprites/enemy/Bullet.png').convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))
        self.speed = 5
        self.direction = dir
        self.points = 0
        self.sound = pygame.mixer.Sound('sounds/enemy_shoot.wav')
        self.sound.set_volume(0.1)
        self.sound.play()
    
    def on_hit(self):
        pass