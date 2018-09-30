#module for bomb
import pygame
from settings import *
bombtime=5
class bomb():
    def __init__(self,x,y):
        self.timer=5
        self.pos=[x,y]
        self.speed=[0,0]
        self.blown=False
    def thrown(self,xsp,ysp):
        self.speed=[xsp+1,ysp+1]
    def move(self):
        self.pos[0]+=self.speed[0]
        self.pos[1]+=self.speed[1]
        if self.speed[0]>0:
            self.speed[0]-=0.2
        if self.speed[1]>0:
            self.speed[1]-=0.2
    def setpos(self,x,y):
        self.pos=[x,y]
    def reducetime(self):
        self.timer-=1
    def gettime(self):
        return self.timer
    def blowup(self):
        self.blown=True
    def draw(self):
        self.image = pygame.image.load('bomb.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]
        screen.blit(self.image, self.rect)

        
