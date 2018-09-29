import pygame 
from settings import *
import random
pygame.init()

pygame.display.update()
clock = pygame.time.Clock()

#initialize objects here

while True:
    
   
    screen.fill(black)
    #Draw board here
    keys = pygame.key.get_pressed()  #checking pressed keys here
    if keys[pygame.K_UP]:
        
    elif keys[pygame.K_DOWN]:
        
        
    elif keys[pygame.K_LEFT]:
        
        
    elif keys[pygame.K_RIGHT]:
        
        

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
    
    #render elements here
    
    pygame.display.update()
    clock.tick(60) 