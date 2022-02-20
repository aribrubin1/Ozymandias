import pygame
class Spot:
    def __init__(self,row,col,width,total_rows,total_cols):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.total_cols = total_cols
        self.x = row*width
        self.y = col*width
        self.colour=(255,255,255)
        self.rect=pygame.Rect(self.x,self.y,self.width,self.width)
        self.wall=False
        self.open = False
        self.closed = False

    def __str__(self):
        stringy = str(self.row)+ " "+str(self.col)
        return stringy

    def update_neighbors(self,grid):
        self.neighbors = []
        if self.row > 0 and grid[self.row-1][self.col].wall == False:#UP
            self.neighbors.append(grid[self.row-1][self.col])
        if self.row < self.total_rows -1 and grid[self.row+1][self.col].wall==False:#DOWN
            self.neighbors.append(grid[self.row+1][self.col])
        if self.col > 0 and grid[self.row][self.col-1].wall==False:#LEFT
            self.neighbors.append(grid[self.row][self.col-1])
        if self.col < self.total_cols - 1 and grid[self.row][self.col+1].wall==False:#RIGHT
            self.neighbors.append(grid[self.row][self.col+1])

    def update_all_neighbors(self,grid):
        self.allneighbors = []
        if self.row > 0:#UP
            self.allneighbors.append(grid[self.row-1][self.col])
        if self.row < self.total_rows -1:#DOWN
            self.allneighbors.append(grid[self.row+1][self.col])
        if self.col > 0:#LEFT
            self.allneighbors.append(grid[self.row][self.col-1])
        if self.col < self.total_cols - 1:#RIGHT
            self.allneighbors.append(grid[self.row][self.col+1])

    def get_pos(self):
        return self.row,self.col

    def make_barrier(self):
        self.wall=True
        self.colour = (0,0,0)

    def Checkwalls(self,rect):
        if rect.colliderect(self):
            return True
        for i in self.neighbors:
            if rect.colliderect(i):
                return True
            for g in i.neighbors:
                if rect.colliderect(g):
                    return True
        return False