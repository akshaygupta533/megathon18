#module for bomb
bombtime=5
class bomb():
    def __init__(self,x,y):
        self.timer=5
        self.pos=[x,y]
        self.speed=[0,0]
        self.blown=False
    def thrown(self,xsp,ysp):
        self.speed=[xsp+1,ysp+1]
    def move(self):
        self.pos+=self.speed
        if self.speed[0]>0:
            self.speed[0]-=0.1
        if self.speed[1]>0:
            self.speed[1]-=0.1
    def reducetime(self):
        self.timer-=1
    def gettime(self):
        return self.timer
    def blowup(self):
        self.blown=True
        
