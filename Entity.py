#module for player
from settings import *
import pygame

class Character():
    def __init__(self, health, canthrow, speedx, speedy, x, y, armour):
        self.health = health
        self.canthrow = canthrow
        self.speedx = speedx
        self.speedy = speedy
        self.x = x
        self.y = y
        self.armour = armour
        self.count=5

    def onHit(self, distance):
        if distance<100:
            self.health-=(1/(1+distance))*5550/self.armour
    def reducecount(self):
        self.count-=1
class Player(Character):
    def __init__(self):
        super().__init__(100, True, 1,1, 300, 300,5)

    def movement(self, dir):
        if dir == 'a':
            self.speedX = -1
            self.x += self.speedX
            if(self.x < 40):
                self.x = 40
        elif dir == 'd':
            self.speedX = +1
            self.x += self.speedX
            if(self.x > 1140):
                self.x = 1140
        elif dir == 'w':
            self.speedY = -1
            self.y += self.speedY
            if(self.y < 40):
                self.y = 40
        elif dir == 's':
            self.speedY = +1
            self.y += self.speedY
            if(self.y > 510):
                self.y = 510

    def draw(self):
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        screen.blit(self.image, self.rect)
