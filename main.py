import pygame
import random
import sys
from enemy import *
from Entity import *
from bomb import *
from bombthrow import *
from board import *

pygame.init()

clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
brown = (255,64,64)

w,h = 1200,600
screen = pygame.display.set_mode((w,h))
line_width = 10

board = Board(screen,w,h)
player = Player()
#initialize objects here

while True:
    screen.fill(black)
    board.draw()
    player.draw()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.movement('a')

    if keys[pygame.K_d]:
        player.movement('d')

    if keys[pygame.K_w]:
        player.movement('w')

    if keys[pygame.K_s]:
        player.movement('s')

    if keys[pygame.K_q]:
        break
    #render elements here

    pygame.display.update()
    pygame.event.pump()
clock.tick(60)
