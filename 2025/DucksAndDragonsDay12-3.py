from collections import deque

grid = [[int(i) for i in y] for y in open('day12-3in.txt').read().split('\n')]

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
 
def greedy_best_three(grid):
    rows, cols = len(grid), len(grid[0])
     
    reachable_sets = {}
    for r in range(len(grid)):
        print(r)
        for c in range(len(grid[0])):
            reachable_sets[(r,c)] = compute_reachable(grid,(r,c))

    first = max(reachable_sets.keys(), key=lambda k: len(reachable_sets[k]))
    chosen = [first]
    covered = set(reachable_sets[first])
 
    for _ in range(2):
        best_cell = None
        best_gain = -1
        for cell, reach in reachable_sets.items():
            if cell in chosen:
                continue
            gain = len(reach - covered)  
            if gain > best_gain:
                best_gain = gain
                best_cell = cell
        chosen.append(best_cell)
        covered |= reachable_sets[best_cell]
 
    return chosen, len(covered)
 

best_points, max_cover = greedy_best_three(grid)
print(max_cover)
