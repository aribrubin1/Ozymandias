import pygame,sys
from Variables import *
from Objects.Player import Player
from Game import Game

#Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('DungeonCrawler')
NewGame = Game(100,screen,clock)
while True:
    NewGame.GameLoop()
