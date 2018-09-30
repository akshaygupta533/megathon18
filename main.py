import pygame
import random
import sys
from enemy import *
from Entity import *
from bomb import *
from bombthrow import *
from board import *
import time

pygame.init()
initial_time = time.time()
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
enemylist=[]
bomblist=[]
playerbomb=bomb(10,10)
flag = False
for i in range(3):
    rand1=randint(600,1100)
    rand2=randint(50,550)
    rand3=randint(20,100)/250
    rand4=randint(20,100)/250
    en=enemy(100,True,rand3,rand4,rand1,rand2,50,rand3,rand4)
    enemylist.append(en)
#initialize objects here

while True:
    # print(player.health)
    screen.fill(black)
    final_time = time.time()
    if((int)(final_time) - (int)(initial_time) == 1):
        #print((int)(final_time) - (int)(initial_time))
        flag = True
        initial_time = final_time
    board.draw()
    player.draw()
    blastshow(bomblist,playerbomb)
    throwbomb=False
    bombthrow(board,player,enemylist,bomblist,throwbomb,playerbomb)
    drawbomb(board,bomblist,playerbomb)
    damageHandeler(board,player,enemylist,bomblist,playerbomb)
    for i in enemylist:
        i.draw(player.x,player.y,5)
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
    if flag==True:
        for i in bomblist:
            i.reducetime()
        for i in bomblist:
            if i.blast==True:
                i.blast=False
        if playerbomb.blast==True:
            playerbomb.blast=False
        for i in enemylist:
            if i.canthrow==False:
                if i.count==0:
                    i.canthrow=True
                    i.count=5
                else:
                    i.reducecount()
        if player.canthrow==False:
            if player.count==0:
                player.canthrow=True
                player.count=5
            else:
                player.reducecount()
        
        flag=False
    pygame.display.update()
    pygame.event.pump()
clock.tick(60)
