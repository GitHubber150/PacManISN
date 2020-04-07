import pygame

class point(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.alive = 1
        self.image = pygame.image.load('assets/point.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
