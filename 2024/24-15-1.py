f = [i for i in open('24-15-1.txt').read().split('\n')]

# Managed to get 42nd on the global leaderboard. A* search engine.

from collections import deque

def find_shortest_path(maze):
    rows, cols = len(maze), len(maze[0])
    
    # Find the entry point
    entry = None
    for i in range(rows):
        for j in range(cols):
            if (i == 0 or i == rows-1 or j == 0 or j == cols-1) and maze[i][j] == '.':
                entry = (i, j)
                break
        if entry:
            break
    
    def bfs(start, target):
        queue = deque([(start, [])])
        visited = set([start])
        
        while queue:
            (x, y), path = queue.popleft()
            
            if maze[x][y] == target:
                return path + [(x, y)]
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#' and (nx, ny) not in visited:
                    queue.append(((nx, ny), path + [(x, y)]))
                    visited.add((nx, ny))
        
        return None
    
    # Find path from entry to 'H'
    path_to_h = bfs(entry, 'H')
    if not path_to_h:
        return None
    
    # Find path from 'H' back to entry
    path_to_entry = bfs(path_to_h[-1], '.')
    if not path_to_entry:
        return None
    
    # Combine paths
    return path_to_h + path_to_entry[1:]

# Example usage
maze = [
    ['#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '#'],
    ['#', '.', '#', '.', '#'],
    ['#', '.', 'H', '.', '#'],
    ['#', '#', '#', '#', '#']
]



result = find_shortest_path(f)
print(2* (len(result)-2))
if result:
    print("Shortest path:", result)
else:
    print("No valid path found")
