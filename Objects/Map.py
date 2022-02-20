from PathFinder.make_grid import make_grid
from Variables import *
class Map:
    def __init__(self,screen,width,height):
        self.grid = make_grid(int(width/GRIDWIDTH),int(height/GRIDWIDTH),GRIDWIDTH)
        self.screen= screen
        #self.gatherwalls()

    def neighbormaker(self):
        for row in self.grid:
            for spot in row:
                spot.update_neighbors(self.grid)
                spot.update_all_neighbors(self.grid)

    def gatherwalls(self):
        self.Walls = []
        for i in self.grid:
            for spot in i:
                if i.wall==True:
                    self.Walls.append(i)