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

    def onHit(self, distance):
        self.health-=(1/(1+distance))*0.5/self.armour

class Player(Character):
    def __init__(self):
        super().__init__(100, True, 1,1, 300, 300,5)

    def movement(self, dir):
        if dir == 'a':
            self.speedX = -1
            self.x += self.speedX
        elif dir == 'd':
            self.speedX = +1
            self.x += self.speedX
        elif dir == 'w':
            self.speedY = -1
            self.y += self.speedY
        elif dir == 's':
            self.speedY = +1
            self.y += self.speedY

    def draw(self):
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        screen.blit(self.image, self.rect)
