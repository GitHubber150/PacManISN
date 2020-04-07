import pygame
import time as t

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.alive = 1
        self.life_amount = 3
        self.default_life_amount = 3
        self.velocity = 15
        self.default_velocity = 5
        self.image = pygame.image.load('assets/pac-man.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1080/2
        self.rect.y = 720/2

    def move_right(self):
        self.rect.x += self.velocity
        self.image = pygame.image.load('assets/pac-man-right.png')

    def move_left(self):
        self.rect.x -= self.velocity
        self.image = pygame.image.load('assets/pac-man-left.png')

    def move_down(self):
        self.rect.y += self.velocity
        self.image = pygame.image.load('assets/pac-man-down.png')
        
    def move_up(self):
        self.rect.y -= self.velocity
        self.image = pygame.image.load('assets/pac-man-up.png')
