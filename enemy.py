import pygame
from settings import *


class enemy:
    def __init__(self):
        self.x = 150
        self.y = 300
    def draw(self,targetx,targety,radius):
        prev_x = self.x
        prev_y = self.y
        if targetx - self.x>0:
            self.x+=1
        elif targetx - self.x<0:
            self.x-=1
        
        if targety - self.y>0:
            self.y+=1
        elif targety - self.y<0:
            self.y-=1
        
        if math.sqrt((self.x - targetx)**2 + (self.y - targety)**2)<radius**2:
            self.x = prev_x
            self.y = prev_y

        self.image = pygame.image.load('rsz_1enemy.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        screen.blit(self.image, self.rect)