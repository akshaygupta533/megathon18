# player and enemy functions (bombthrow and damage)
from player import *
from bomb import *
import math

#make throwbomb true if plaer presses button for bomb throw
def bombthrow(board,player,enemylist,bomblist,throwbomb,playerbomb):
    for i in enemylist:
        if i.canthrow == True:
            if(i.speedx!=0 or i.speedy!=0):
                bombinst=bomb(i.x,i.y)
                bomblist.append(bombinst)
                bomblist[len(bomblist)-1].throw(i.speedx,i.speedy)
    
    if throwbomb==True:
        playerbomb=bomb(player.x,player.y)
        playerbomb.throw(player.speedx,player.speedy)
    return playerbomb
        #make throwbomb false in main.py
    
def drawbomb(board,bomblist):
    pass

def damageHandeler(board,player,enemylist,bomblist,playerbomb):
    for i in bomblist:
        if i.gettime()==0 and not i.blown:
            i.blowup()
            d=math.sqrt((i.pos[0]-player.x)*(i.pos[0]-player.x)+(i.pos[1]-player.y)*(i.pos[1]-player.y))
            player.onHit(d)
    
    if playerbomb.gettime()==0 and not playerbomb.blown:
        i.blowup()
        for i in enemylist:
            d=math.sqrt((playerbomb.pos[0]-i.x)*(playerbomb.pos[0]-i.x)+(playerbomb.pos[1]-i.y)*(playerbomb.pos[1]-i.y))
            i.onHit(d)    