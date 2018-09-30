import pygame
from settings import *
from Entity import *

class enemy(Character):
    def __init__(self,health, canThrow, speedx, speedy, x, y, armour):
        super().__init__(health, canThrow, speedx, speedy, x, y, armour)

    def onHit(self, distance):
        super().onHit(distance)

    def draw(self,targetx,targety,radius):
        prev_x = self.x
        prev_y = self.y
        if targetx - self.x>0:
            self.speedx=1
            self.x+=self.speedx
        elif targetx - self.x<0:
            self.speedx=-1
            self.x+=self.speedx
        
        if targety - self.y>0:
            self.speedy=1
            self.y+=self.speedy
        elif targety - self.y<0:
            self.speedy=-1
            self.y+=self.speedy
        
        if math.sqrt((self.x - targetx)**2 + (self.y - targety)**2)<radius:
            self.x = prev_x
            self.y = prev_y

        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        screen.blit(self.image, self.rect)