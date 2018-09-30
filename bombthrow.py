# player and enemy functions (bombthrow and damage)
from Entity import *
from bomb import *
import math

#make throwbomb true if plaer presses button for bomb throw
#playerbomb is player's bomb
def bombthrow(board,player,enemylist,bomblist,throwbomb,playerbomb):
    for i in enemylist:
        #print(i.canthrow)
        if i.canthrow == True:
            if(i.speedx!=0 or i.speedy!=0):
                bombinst=bomb(i.x,i.y)
                bomblist.append(bombinst)
                bomblist[len(bomblist)-1].thrown(i.speedx+(player.x-i.x)*2/abs((player.x-i.x)),i.speedy+(player.y-i.y)*2/abs((player.y-i.y)))
            i.canthrow=False
    if throwbomb==True:
        playerbomb=bomb(player.x,player.y)
        playerbomb.thrown(player.speedx+2,player.speedy+2)
    return playerbomb
        #make throwbomb false in main.py
    
def drawbomb(board,bomblist,playerbomb):
    for i in bomblist:   
        if not i.blown:
            i.draw()
            i.move()
    if not playerbomb.blown:
        playerbomb.draw()
        playerbomb.move()

def damageHandeler(board,player,enemylist,bomblist,playerbomb):
    for i in bomblist:
        if i.gettime()==0 and not i.blown:
            i.blowup()
            i.blast=True
            d=math.sqrt((i.pos[0]-player.x)*(i.pos[0]-player.x)+(i.pos[1]-player.y)*(i.pos[1]-player.y))
            player.onHit(d)
            #i.blown=True
    
    if playerbomb.gettime()==0 and not playerbomb.blown:
        playerbomb.blowup()
        playerbomb.blast=True
        for i in enemylist:
            d=math.sqrt((playerbomb.pos[0]-i.x)*(playerbomb.pos[0]-i.x)+(playerbomb.pos[1]-i.y)*(playerbomb.pos[1]-i.y))
            i.onHit(d)

def blastshow(bomblist,playerbomb):
    for i in bomblist:
        if i.blast==True:
            image = pygame.image.load('blast.png')
            rect = image.get_rect()
            rect.centerx = i.pos[0]
            rect.centery = i.pos[1]
            screen.blit(image, rect)
    if playerbomb.blast==True:
        image = pygame.image.load('blast.png')
        rect = image.get_rect()
        rect.centerx = i.pos[0]
        rect.centery = i.pos[1]
        screen.blit(image, rect)