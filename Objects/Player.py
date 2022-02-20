from Objects.BaseObject import GameObject
import pygame
from Variables import *
class Player(GameObject):
    def __init__(self, rect, Health,screen,grid):
        super().__init__(rect)
        self.velocity = 3
        self.Health = Health
        self.MaxHealth = Health
        self.centrex = self.rect.x+int(PLAYERLENGTH/3)
        self.centrey = self.rect.y+int(PLAYERLENGTH/3)
        self.gridpos = [int(round(self.centrex/GRIDWIDTH)),int(round(self.centrey/GRIDWIDTH))]
        self.screen = screen
        self.grid = grid
        self.history = []

    def MoveRight(self):
        self.checkout()

        if self.collisiondetect("R"):
            return
        self.rect.x += self.velocity
        self.centrex = self.rect.x + int(PLAYERLENGTH / 2)
        self.gridpos[0] = int(round(self.centrex/GRIDWIDTH))
        self.checkout()


    def MoveLeft(self):
        self.checkout()
        if self.collisiondetect("L"):
            return
        self.rect.x -= self.velocity
        self.centrex = self.rect.x + int(PLAYERLENGTH / 2)
        self.gridpos[0] = int(round(self.centrex / GRIDWIDTH))
        self.checkout()

    def MoveUp(self):
        self.checkout()
        if self.collisiondetect("U"):
            return
        self.rect.y -= self.velocity
        self.centrey = self.rect.y+int(PLAYERLENGTH/2)
        self.gridpos[1] = int(round(self.centrey / GRIDWIDTH))
        self.checkout()

    def MoveDown(self):
        self.checkout()
        if self.collisiondetect("D"):
            return
        self.rect.y += self.velocity
        self.centrey = self.rect.y+int(PLAYERLENGTH/2)
        self.gridpos[1] = int(round(self.centrey / GRIDWIDTH))
        self.checkout()

        if self.grid[self.gridpos[0]][self.gridpos[1]].wall:
            self.gridpos[1]-=1

    def collisiondetect(self,move):
        if move == "R":
            newrect = pygame.Rect(self.rect.x+self.velocity, self.rect.y, PLAYERLENGTH, PLAYERLENGTH)
        if move == "L":
            newrect = pygame.Rect(self.rect.x-self.velocity, self.rect.y, PLAYERLENGTH, PLAYERLENGTH)
        if move == "U":
            newrect = pygame.Rect(self.rect.x, self.rect.y-self.velocity, PLAYERLENGTH, PLAYERLENGTH)
        if move == "D":
            newrect = pygame.Rect(self.rect.x, self.rect.y+self.velocity, PLAYERLENGTH, PLAYERLENGTH)
        if move == "P":
            newrect = self.rect

        if self.grid[self.gridpos[0]][self.gridpos[1]].wall and newrect.colliderect(self.grid[self.gridpos[0]][self.gridpos[1]]):
            return True

        for i in self.grid[self.gridpos[0]][self.gridpos[1]].allneighbors:
            if i.wall and newrect.colliderect(i):
                return True
            for n in i.allneighbors:
                if n.wall and newrect.colliderect(n):
                    return True
        return False

    def checkout(self):
        if self.gridpos[0]==30:
            self.gridpos[0]-=1
        if self.gridpos[1]==16:
            self.gridpos[1]-=1

    def rollback(self):
        while self.collisiondetect("P") and len(self.history)!=0:
            print("rollback")
            lastplace = self.history.pop()
            self.rect.x = lastplace[0]
            self.rect.y = lastplace[1]