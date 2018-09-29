#module for player
speedy=speedx=3
bombRenewCount=5
class player():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.health=3
        self.speedx=speedx
        self.speedy=speedy
        self.bombRenewCount=bombRenenewCount
    
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    
    def getspeedx(self):
        return self.speedx
    def getspeedx(self):
        return self.speedx
    
    def gethealth(self):
        return self.health
    def reducehealth(self,distance):
        if distance>5: #change this constant
            self.health-=(1/(1+distance))*0.5 #change this constant: hit and trial
    def increasehealth(self):
        self.health+=1
    
    def renderPlayer(self,board):
        #your code here
        pass
        #
    
    
