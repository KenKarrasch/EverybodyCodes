
g = open('24-20-2.txt').read().split('\n')

map_ = []
for i in g:
    lst = []
    for j in i:
        lst.append(j)
    map_.append(lst)


import heapq

# Directions for movement: up, down, left, right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Define the map
mp_ = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', '.', '-', '.', 'A', '#'],
    ['#', '.', '#', '.', '#', '.', '#'],
    ['#', '.', '.', '-', '.', 'B', '#'],
    ['#', '#', '.', '.', '.', 'C', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]

# Function to check if a position is within bounds and not a wall
def is_valid(x, y, map_):
    return 0 <= x < len(map_) and 0 <= y < len(map_[0]) and map_[x][y] != '#'

# Function to calculate time penalty based on the tile
def get_time_penalty(tile):
    if tile == '-':
        return 2
    elif tile == '.':
        return 1
    else:
        return -1
            
def get_height(tile):
    if tile == '-':
        return -2
    elif tile == '.':
        return -1
    elif tile in 'SABC':
        return -1
    return 1

def drawmap(path):
    print(path)
    for i in range(len(map_)):
        ln = ''
        for j in range(len(map_[i])):
            if (i,j) in path:
                ln = ln + '*'
            else:
                ln = ln + map_[i][j]
        print(ln)

# Function to find the shortest path visiting waypoints in order
def find_ordered_path(start, waypoints, map_):
    # Priority queue: (current_time, x, y, current_waypoint_index)
    pq = [(0, start[0], start[1], 0, start, [], 0, 10000, [])]
    visited_states = set()

    print(waypoints)

    DP = {}

    fs = 0
    mn = 10000000

    ct = 0
    ht = 0
    
    samples = []
    cand = []
    best = 1000000

    while pq:
        current_time, x, y, waypoint_index, previous, path, steps, height, kvisited  = heapq.heappop(pq)
        
        ct += 1
        if ct%10000 == 0:
            print('ct',ct,len(DP))
        #print(kvisited)
        # If all waypoints have been visited in order and returned to start, return the time        
        if waypoint_index == len(waypoints): # and height >= 10000:         
            fs += 1
            mn = min(mn,current_time)
            #print(path,current_time,steps,mn)            
            if best > steps + (10000-height):
                drawmap(nkvisited)
                print('new best', steps + (10000-height))
                print('diff', steps - (10000-height))
                print(current_time,steps,height,'best time',steps + (10000-height))#,path)
                
                
            best = min(best, steps + (10000-height))            

            #if best + 5 > steps + (10000-height):
                #print('interesting',current_time,steps,height,steps + (10000-height))#,path)
            #print(current_time,steps,height,steps + (10000-height), best)
            if height >= 10000: 
                samples.append(steps)
            
            #cand.append([steps + (10000-height),steps,height])
            #print(DP)
            if fs > 10000:
                #print(path,current_time,steps,height,mn)
                #print(current_time,steps,height,mn)
                #print(min(samples))

                return current_time
                
        if (x, y, waypoint_index) in DP: #, previous[0], previous[1]) in DP:
            if(current_time >= DP[(x, y, waypoint_index)]):#, previous[0], previous[1])]):
                ht += 1
                #print('hit',ht)      
                continue
            else:
                #print('quicker route found')
                #if not (3 <= x < 4 and 77 <= y < 79) and waypoint_index < len(waypoints):
                    DP[(x, y, waypoint_index)] = current_time # , previous[0], previous[1])
        else:
            #if not (3 <= x < 4 and 77 <= y < 79) and waypoint_index < len(waypoints):
                DP[(x, y, waypoint_index)] = current_time  # , previous[0], previous[1])

        # Skip if this state has been visited
        #if (x, y, waypoint_index) in visited_states:
            #if((x,y) not in cvt):
        #        continue
        #visited_states.add((x, y, waypoint_index))
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy            
            if (nx, ny) != previous:
                if True: # (nx,ny) not in kvisited:
                    if is_valid(nx, ny, map_):
                        #print(nx,ny)
                        new_time = current_time + 1 + get_time_penalty(map_[nx][ny])
                        nheight = height + get_height(map_[nx][ny])
                        npath = path[:]
                        npath.append(x) 
                        npath.append(y) 
                        npath.append(height) 
                        npath.append(new_time)
                        npath.append('|')  
                        nkvisited = []
                        for kv in kvisited:
                            nkvisited.append((kv[0],kv[1]))
                        nkvisited.append((nx,ny))
                        # If we reach the next waypoint in the sequence, increment the waypoint index
                        if waypoint_index < len(waypoints) and (nx, ny) == waypoints[waypoint_index]:
                            #if(waypoint_index == 3):
                            #print('found path',npath, steps+1, nheight)                            
                            heapq.heappush(pq, (new_time, nx, ny, waypoint_index + 1, (x,y), npath, steps+1, nheight, nkvisited))
                        else:
                            # Otherwise, continue exploring
                            heapq.heappush(pq, (new_time, nx, ny, waypoint_index, (x,y), npath, steps+1, nheight, nkvisited))
    
    return float('inf')  # If no valid path is found

# Define the positions for S, A, B, C
start = (1, 1)  # S
A = (1, 5)      # A
B = (3, 5)      # B
C = (4, 5)      # C
waypoints = [A, B, C, start]  # Ordered waypoints to visit

def find_checkpoints(grid):
    checkpoints = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] not in ['#', '.', '+', '-']:# and grid[i][j] != 'S':
                checkpoints[grid[i][j]] = (i, j)                
    return checkpoints

cp = find_checkpoints(map_)

#waypoints = [cp['S'], cp['A'], cp['B'], cp['C']]

fs = cp['S'][:]


waypoints = [(fs[0],fs[1]), cp['A'], cp['B'], cp['C'],(fs[0],fs[1])]
print('waypoints',waypoints)


# Find the shortest path visiting waypoints in order
total_time = find_ordered_path((fs[0],fs[1]), waypoints[1:], map_)

# not 562
# not 564
# not 565
# not 566
# not 567
# not 568

# ans 578
