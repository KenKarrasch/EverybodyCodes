f = [i for i in open('24-15-3.txt').read().split('\n')]

# puzzle is in three compartments.   It is not obvious until impossible to get hidy holes are plugged.  Wrote
# extension to plug the holes, visualises each compartment explorations.  Assumes ABCDE are in the left compartment etc.
# Got 41 on the global leaderboard

from collections import deque

def find_shortest_path(maze,letters):
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
    
    def bfs(start,letters):
        queue = deque([(start, [], set())])
        visited = set([(start[0], start[1], frozenset())])
        ll = len(letters)
        while queue:
            (x, y), path, collected = queue.popleft()
            
            if maze[x][y] in letters: #'ghijer':#'ONPQR':#'ABCDE':
                collected = collected.union({maze[x][y]})
            
            if len(collected) == ll and (x, y) == entry:
                return path
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < rows and 0 <= ny < cols and 
                    maze[nx][ny] in 'QWERTYUIOPASDFGHJKLZXCVBNM.' and #maze[nx][ny] not in '#~' and 

                    ((nx, ny, frozenset(collected))) not in visited):
                    queue.append(((nx, ny), path + [(x, y)], collected))
                    visited.add((nx, ny, frozenset(collected)))
        
        return None

    shortest_path = bfs(entry,letters)
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

if True:
    fn = []
    fnd = True
    while fnd:
        print('rationalising grid')
        fn = []
        fnd = False
        for x in range(len(f)):
            row = []
            for y in range(len(f[0])):
                edges = 0
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < len(f) and 0 <= ny < len(f[0])) and f[nx][ny] == "#":
                        edges += 1                    
                if((edges > 2) and (f[x][y] == ".")):
                    fnd = True
                if (f[x][y] == "#") or edges > 2:
                    row.append('#')                        
                else: row.append(f[x][y])
            fn.append(row)
        f = [i for i in [r for r in fn]]
    print('done')



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
        elif visual_maze[x][y] in 'ABCDEIHJGONPQR':
            pass  # Leave A, B, C, D, E as they are
        else:
            visual_maze[x][y] = 'o'  # Path
    
    
    for row in visual_maze:
    
        print(''.join(row))
    
# Visualize the path


leftportal = find_shortest_path(f,'ABCDE')
if leftportal[1]:
    print("\nVisualized path - Left Portal:")
    visualize_path(f, leftportal[1])
centreportal = find_shortest_path(f,'IHJGER')
if centreportal[1]:
    print("\nVisualized path - Centre Portal:")
    visualize_path(f, centreportal[1])
rightportal = find_shortest_path(f,'ONPQR')
if rightportal[1]:
    print("\nVisualized path - Right Portal:")
    visualize_path(f, rightportal[1])
leftportalentry = find_shortest_path(f,'R')
if leftportalentry[1]:
    print("\nVisualized path - Left Portal Entry:")
    visualize_path(f, leftportalentry[1])
rightportalentry = find_shortest_path(f,'E')
if rightportalentry[1]:
    print("\nVisualized path - Right Portal Entry:")
    visualize_path(f, rightportalentry[1])
print(leftportal[0],centreportal[0],rightportal[0],leftportalentry[0],rightportalentry[0])

print('part 3 - ', leftportal[0] + centreportal[0] + rightportal[0] - (leftportalentry[0] + rightportalentry[0]))
