f = [i for i in open('24-15-2.txt').read().split('\n')]

# Managed to get 28th on the global leaderboard. A* search engine, has visualisation of path

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
    
    def bfs(start):
        queue = deque([(start, [], set())])
        visited = set([(start[0], start[1], frozenset())])
        
        while queue:
            (x, y), path, collected = queue.popleft()
            
            if maze[x][y] in 'ABCDE':
                collected = collected.union({maze[x][y]})
            
            if len(collected) == 5 and (x, y) == entry:
                return path
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < rows and 0 <= ny < cols and 
                    maze[nx][ny] not in '#~' and 
                    ((nx, ny, frozenset(collected))) not in visited):
                    queue.append(((nx, ny), path + [(x, y)], collected))
                    visited.add((nx, ny, frozenset(collected)))
        
        return None

    shortest_path = bfs(entry)
    return len(shortest_path) if shortest_path else None, shortest_path

# Example usage
maze = [
    ['#', '#', '#', '.', '#', '#', '#'],
    ['#', 'A', '.', '.', 'D', 'B', '#'],
    ['#', '~', '#', '#', '#', '.', '#'],
    ['#', 'E', '.', '.', '~', '.', '#'],
    ['#', 'C', '#', '#', '#', 'A', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]

result = find_shortest_path(f)
if result[0]:
    print("Shortest path length:", result[0])
    print("Path:", result[1])
else:
    print("No valid path found")

# Function to visualize the path in the maze
def visualize_path(maze, path):
    #visual_maze = [row[:] for row in maze]
    visual_maze = []
    for r in maze:
        ln = []
        for i in r:
            ln.append(i)
        visual_maze.append(ln)
    for i, (x, y) in enumerate(path):
        if i == 0:
            visual_maze[x][y] = 'S'  # Start
        elif i == len(path) - 1:
            visual_maze[x][y] = 'E'  # End
        elif visual_maze[x][y] in 'ABCDE':
            pass  # Leave A, B, C, D, E as they are
        else:
            visual_maze[x][y] = 'o'  # Path
    
    for row in visual_maze:
        print(' '.join(row))

# Visualize the path
if result[1]:
    print("\nVisualized path:")
    visualize_path(f, result[1])
