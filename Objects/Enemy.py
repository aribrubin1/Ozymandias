from Objects.BaseObject import GameObject
from PathFinder.PathFind import PathFind
from Variables import *
import pygame
class Enemy(GameObject):
    def __init__(self,rect):
        super().__init__(rect)
        self.xspeed = 0.2
        self.yspeed = 0.2
        self.maxspeed = 1.5
        self.xdirection = 0
        self.ydirection = 0
        self.colour=(255,0,0)

        self.centrex = self.rect.x + int(PLAYERLENGTH / 2)
        self.centrey = self.rect.y + int(PLAYERLENGTH / 2)
        self.gridpos = [int(round(self.centrex / GRIDWIDTH)), int(round(self.centrey / GRIDWIDTH))]

        self.path = None

    def setpath(self,Player,Map):
        if self.gridpos==Player.gridpos:
            self.path= None
            return
        self.path = PathFind(Map.grid,Map.grid[self.gridpos[0]][self.gridpos[1]],Map.grid[Player.gridpos[0]][Player.gridpos[1]])
        self.path.reverse()
        for i in self.path:
            pygame.draw.rect(Map.screen,(0,0,0),(i.x,i.y,50,50))

    def Move(self):
        if self.path != None and len(self.path)!=0:
            if self.path[0].x < self.rect.x:
                self.rect.x-=1
            elif self.path[0].x > self.rect.x:
                self.rect.x += 1
            elif self.path[0].y < self.rect.y:
                self.rect.y-= 1
            elif self.path[0].y > self.rect.y:
                self.rect.y+=1
            else:
                self.path.pop(0)

        else:
            self.path = None

        self.centrex = self.rect.x + int(PLAYERLENGTH / 2)
        self.centrey = self.rect.y + int(PLAYERLENGTH / 2)
        self.gridpos = [int(round(self.centrex / GRIDWIDTH)), int(round(self.centrey / GRIDWIDTH))]
        if self.gridpos[1]==16:
            self.gridpos[1]-=1
        if self.path==0:
            self.path=None

    def secondarymove(self,Player):
        if self.rect.x < Player.rect.x:
            self.rect.x+=1
        elif self.rect.x > Player.rect.x:
            self.rect.x-=1
        elif self.rect.y < Player.rect.y:
            self.rect.y+=1
        elif self.rect.y > Player.rect.y:
            self.rect.y-=1


    def CheckOut(self,Player):
        if Player.gridpos == self.gridpos:
            self.path = None