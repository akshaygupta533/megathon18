#module for player

class Character(self):
    def __init__(self, health, canThrow, speedX, speedY, speedWithBomb, x, y, armour, icon):
        self.health = health
        self.canThrow = canThrow
        self.speedX = speedX
        self.speedY = speedY
        self.speedWithBomb  = speedWithBomb
        self.x = x
        self.y = y
        self.armour = armour
        self.icon = icon

    def onHit(self, distance):
        self.health-=(1/(1+distance))*0.5/self.armour


class Enemy1(Character):
    def __init__(self):
        super().__init__(100, True, 5, 5, 3, randInt(5, 1195), randInt(5, 595), 10, pygame.image.load("Enemy1.png"))


class Enemy2(Character):
    def __init__(self):
        super().__init__(150, True, 10, 10, 5, randInt(5, 1195), randInt(5, 595), 15, pygame.image.load("Enemy1.png"))


class Player(Character):        
    def __init__(self):
        super().__init__(100, True, 5, 5, 3, randInt(5, 1195), randInt(5, 595), 10, pygame.image.load("Player.png"))

def movement(self, dir):
        if dir == 'a':
            self.x -= self.speed
        elif dir == 'd'
            self.x += self.speed
        elif dir == 'w'
            self.y += self.speed    
        elif dir == 's'
            self.y -= self.speed



