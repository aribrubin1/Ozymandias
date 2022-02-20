import random
class Snake:
    def __init__(self,startpos,grid,length):
        self.grid = grid
        self.pos = startpos
        print(self.pos)
        self.currentspot = grid[startpos[1]][startpos[0]]
        self.length = length
        self.move([random.randint(0,1),random.randint(0,1)])
        self.length = length
        self.move([random.randint(0, 1), random.randint(0, 1)])

    def updatespot(self):
        self.currentspot = self.grid[self.pos[1]][self.pos[0]]

    def move(self,dir):
        #at [0] 0 means on x and 1 means y
        #at [1] 0 means (+) and 1 means (-)
        self.currentspot.make_barrier()
        if dir[0]==0 and dir[1]==0:
            if self.pos[0]==13:
                self.move([1,random.randint(0,1)])
            else:
                self.pos[0]+=1
        elif dir[0] == 0 and dir[1] == 1:
            if self.pos[0] == 3:
                self.move([1,random.randint(0,1)])
            else:
                self.pos[0] -= 1

        elif dir[0] == 1 and dir[1] == 0:
            if self.pos[1] == 27:
                self.move([0, random.randint(0, 1)])
            else:
                self.pos[1] += 1
        elif dir[0] == 1 and dir[1] == 1:
            if self.pos[1] == 3:
                self.move([0, random.randint(0, 1)])
            else:
                self.pos[1] -= 1

        if self.length!=0:
            self.length -=1
            self.updatespot()
            self.move([dir[0],dir[1]])
