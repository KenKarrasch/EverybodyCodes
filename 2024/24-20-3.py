g = open('24-20-3.txt').read().split('\n')

map_ = []
for i in g:
    lst = []
    for j in i:
        lst.append(j)
    map_.append(lst)

mapsize = len(g)

import heapq

# Directions for movement: up, down, left, right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to check if a position is within bounds and not a wall
def is_valid(x, y, map_):
    return 0 <= x and 0 <= y < len(map_[0]) and map_[x%mapsize][y] != '#'

           
def get_height(tile):
    if tile == '-':
        return -2
    elif tile == '.':
        return -1
    elif tile in 'SABC':
        return -1
    return 1

def drawmap(path,x):
    times = 1 + (x//mapsize)
    print()
    for m in range(times):
        for i in range(len(map_)):
            ln = ''
            for j in range(len(map_[i])):
                if (i+m*mapsize,j) in path:
                    ln = ln + '*'
                else:
                    ln = ln + map_[i][j]
            print(ln)

# Function to find the shortest path visiting waypoints in order
def find_ordered_path(start, map_, startheight):
    # Priority queue: (current_time, x, y, current_waypoint_index)
    pq = [(startheight, start[0], start[1], start, [], 0, [])]
    
    DP = {}

    fs = 0    
    ct = 0
    ht = 0
    
    best = 0

    while pq:
        height, x, y, previous, path, steps, kvisited  = heapq.heappop(pq)
        
        ct += 1
        if ct%10000 == 0:
            print('ct',ct,len(DP))      

        if height < 1:        
            fs += 1
            #print('dist',x)            
            if best < x:
                #drawmap(nkvisited,x)
                print('new best', x, 'steps',steps)                                
            best = max(best,x)
            if fs > 30000:                     
                return x
            continue
                
        if (x, y) in DP:
            if height <= DP[(x, y)]:
                ht += 1
                #print('hit',ht)      
                continue
            else:
                #print('quicker route found')
                    DP[(x, y)] = height # , previous[0], previous[1])
        else:
                DP[(x, y)] = height  # , previous[0], previous[1])

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy            
            if (nx, ny) != previous:                
                if is_valid(nx, ny, map_):                        
                    nheight = height + get_height(map_[nx%mapsize][ny])
                    #print('new height',nheight)
                    npath = path[:]
                    npath.append(x) 
                    npath.append(y) 
                    npath.append(height)                         
                    npath.append('|')  
                    nkvisited = []
                    for kv in kvisited:
                        nkvisited.append((kv[0],kv[1]))
                    nkvisited.append((nx,ny))                    
                    heapq.heappush(pq, (nheight, nx, ny, (x,y), npath, steps+1, nkvisited))
    
    return best
#float('inf')  # If no valid path is found


def find_checkpoints(grid):
    checkpoints = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] not in ['#', '.', '+', '-']:# and grid[i][j] != 'S':
                checkpoints[grid[i][j]] = (i, j)                
    return checkpoints

fs = find_checkpoints(map_)
print(fs)

ds = []

for t in range(1,40):
    total_dist = find_ordered_path(fs['S'], map_, t)    
    ds.append([t,total_dist])

for i in ds:
    print(i)

seek = 384400

dist = ds[-1][1]

leap1 = ds[-2][1] - ds[-3][1]
leap2 = ds[-1][1] - ds[-2][1]
lp = leap1
for i in range(seek - ds[-1][0]):
    dist += lp
    if lp == leap1:
        lp = leap2
    else:
        lp = leap1
print(dist)
