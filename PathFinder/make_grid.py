from PathFinder.Spot import Spot
def make_grid(rows,colomns,width):
    grid=[]
    for i in range(rows):
        grid.append([])
        for j in range(colomns):
            spot = Spot(i,j,width,rows,colomns)
            grid[i].append(spot)
    return grid