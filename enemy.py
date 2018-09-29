import pygame
from settings import *
from Entity import *

class enemy(Character):
    def __init__(self,health, canThrow, speedX, speedY, x, y, armour, icon):
        super().__init__(health, canThrow, speedX, speedY, x, y, armour, icon)

    def onHit(self, distance):
        super().onHit(distance)

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