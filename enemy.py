import pygame
from settings import *

class enemy:
    def __init__(self):
        self.x = 150
    def draw(self,img):
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        screen.blit(self.image, self.rect)