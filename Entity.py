#module for player
from settings import *

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


# class Enemy1(Character):
#     def __init__(self):
#         super().__init__(100, True, 5, 5, randInt(5, 1195), randInt(5, 595), 10, pygame.image.load("Enemy1.png"))


# class Enemy2(Character):
#     def __init__(self):
#         super().__init__(150, True, 10, 10, randInt(5, 1195), randInt(5, 595), 15, pygame.image.load("Enemy1.png"))


class Player(Character):        
    def __init__(self):
        super().__init__(100, True, 5,5, 300, 300,5)

    def movement(self, dir):
        if dir == 'a':
            self.speedX = -5
            self.x += self.speedX
        elif dir == 'd':
            self.speedX = +5
            self.x += self.speedX
        elif dir == 'w':
            self.speedY = -5
            self.y += self.speedY   
        elif dir == 's':
            self.speedY = +5
            self.y += self.speedY
    def draw(self):
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        screen.blit(self.image, self.rect)



