from queue import PriorityQueue
def h(p1,p2):
    x1,y1=p1
    x2,y2=p2
    if type(y1) is tuple:
        print("\n",y1)
    return(abs(x1-x2)+abs(y1-y2))

def reconstruct_path(came_from,current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    return path

def PathFind(grid,start,end):
    print("moveing from",start,"to",end)
    count=0
    open_set = PriorityQueue()
    open_set.put((0,count,start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
    open_set_hash = {start}

    while not open_set.empty():

        temp = open_set.get()
        current = temp[2]
        open_set_hash.remove(current)

        if current==end:
            return reconstruct_path(came_from,end)

        for neighbor in current.neighbors:
            temp_g_score = g_score[current]+1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor]=current
                g_score[neighbor]=temp_g_score
                f_score[neighbor]=temp_g_score+h(neighbor.get_pos(),end.get_pos())
                if neighbor not in open_set_hash:
                    count+=1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)

    return reconstruct_path(came_from,end)