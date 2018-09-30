#module for player
from settings import *
import pygame

class Character():
    def __init__(self, health, canThrow, speedX, speedY, x, y, armour):
        self.health = health
        self.canThrow = canThrow
        self.speedX = speedX
        self.speedY = speedY
        self.x = x
        self.y = y
        self.armour = armour

    def onHit(self, distance):
        self.health-=(1/(1+distance))*0.5/self.armour

class Player(Character):
    def __init__(self):
        super().__init__(100, True, 5,5, 300, 300,5)

    def movement(self, dir):
        print(dir)
        if dir == 'a':
            self.speedX = -0.5
            self.x += self.speedX
            if(self.x < 40):
                self.x = 40

        elif dir == 'd':
            self.speedX = +0.5
            self.x += self.speedX
            if(self.x > 1140):
                self.x = 1140

        elif dir == 'w':
            self.speedY = -0.5
            self.y += self.speedY
            if(self.y < 40):
                self.y = 40

        elif dir == 's':
            self.speedY = +0.5
            self.y += self.speedY
            if(self.y > 510):
                self.y = 510

    def draw(self):
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        screen.blit(self.image, self.rect)
