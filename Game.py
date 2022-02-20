from Objects.Player import Player
from Variables import *
import pygame,sys
from GameMachines.MovementMachine import MovementMachine
from GameMachines.MapMachine import MapMachine
from Objects.Enemy import Enemy
from Objects.Map import Map
from MazeMaker.Snake import Snake
import random

class Game:
    def __init__(self,Playerhealth,screen,clock):
        self.cooldown = 0
        self.Playerhealth = Playerhealth
        self.screen = screen
        self.clock = clock
        self.TestSubject = Enemy(pygame.Rect(300, 400, INVADERLENGTH, INVADERLENGTH))
        self.Map = Map(screen,SCREENWIDTH,SCREENHEIGHT)
        self.Player = Player(pygame.Rect(300, 650, PLAYERLENGTH, PLAYERLENGTH), Playerhealth, screen,self.Map.grid)
        Snakes = []
        for i in range(7):
            randspot = [random.randint(0, 13), random.randint(0, 27)]
            Snakes.append(Snake(randspot, self.Map.grid, 5))
        self.Map.neighbormaker()


    def GameLoop(self):
        tempgridpos = list(self.Player.gridpos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()

        MovementMachine(self.Player)
        self.screen.fill(white)


        if tempgridpos != self.Player.gridpos and self.cooldown==0:
            self.cooldown=100
            self.TestSubject.setpath(self.Player,self.Map)
        if self.cooldown!=0:
            self.cooldown-=1

        self.TestSubject.CheckOut(self.Player)
        MapMachine(self.screen, self.Map.grid,self.Player, self.TestSubject)
        self.Player.render(self.screen, blue)

        #Draw player gridpos
        #pygame.draw.rect(self.screen,(0,124,124),self.Map.grid[self.Player.gridpos[0]][self.Player.gridpos[1]].rect)

        # Basic ending lines
        pygame.display.update()
        self.clock.tick(120)
