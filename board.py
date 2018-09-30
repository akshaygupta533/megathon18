import pygame
import time
import sys
from random import *
from pygame.locals import *

clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
brown = (255,64,64)
line_width = 10

class Board:
    def __init__(self,screen,w,h):
        self.screen = screen
        self.w = w
        self.h = h

    def draw(self):
        pygame.draw.rect(self.screen, brown, [0,0,self.w,line_width])	#top_border
        pygame.draw.rect(self.screen, brown, [0,self.h-line_width,self.w,line_width]) #bottom_border
        pygame.draw.rect(self.screen, brown, [0,0,line_width,self.h]) #left_border
        pygame.draw.rect(self.screen, brown, [self.w-line_width,0,line_width,self.h]) #right_border
