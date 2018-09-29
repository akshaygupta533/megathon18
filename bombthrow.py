# player and enemy functions (bombthrow and damage)
from player import *
from bomb import *

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

def damageHandeler(board,player,enemylist,bomblist):
    for i in bomblist:
        if i.gettime()==0:
            i.blowup()
            
            