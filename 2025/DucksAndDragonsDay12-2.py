from collections import deque
 
f = [[int(i) for i in y] for y in open('day12-2in.txt').read().split('\n')]

def compute_reachable(grid, start):
    rows, cols = len(grid), len(grid[0])
    r, c = start
    q = deque([(r, c)])
    visited = set([(r, c)])    
    while q:
        x, y = q.popleft()        
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if (nx, ny) not in visited and grid[nx][ny] <= grid[x][y]:
                    visited.add((nx, ny))
                    q.append((nx, ny))
    return visited

v1 = compute_reachable(f,(0,0))
v2 = compute_reachable(f,((len(f)-1),len(f[0])-1))
print(len(v1.union(v2)))
