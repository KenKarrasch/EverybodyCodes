f = [i for i in open('24-15-2.txt').read().split('\n')]

# Managed to get 28th on the global leaderboard. A* search engine, has visualisation of path

from itertools import product, permutations
from collections import deque

def find_shortest_collect_all_any_order(maze):
    rows, cols = len(maze), len(maze[0])
    
    # Locate entry and targets
    entry = None
    targets = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == '.' and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                entry = (r, c)
            if maze[r][c] in targets:
                targets[maze[r][c]].append((r, c))
    
    if not entry or not all(targets.values()):
        return -1, maze  # Return -1 if entry or any target is missing

    # Combine entry and all targets into a single list of key points
    # For now, include all combinations of one of each target
    all_combinations = list(product(targets['A'], targets['B'], targets['C'], targets['D'], targets['E']))
    
    # Precompute distances between all key points using BFS
    def bfs(start):
        distances = {}
        queue = deque([(start, 0)])
        visited = set()
        visited.add(start)

        while queue:
            (x, y), dist = queue.popleft()
            distances[(x, y)] = dist

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and maze[nx][ny] != '#':
                    queue.append(((nx, ny), dist + 1))
                    visited.add((nx, ny))

        return distances

    # Build a distance matrix for all key points in a given combination
    def build_distance_matrix(points):
        dist_matrix = {}
        for i, point1 in enumerate(points):
            distances = bfs(point1)
            #print(bfs)
            for j, point2 in enumerate(points):
                if point2 in distances:
                    dist_matrix[(i, j)] = distances[point2]
                else:
                    dist_matrix[(i, j)] = float('inf')
        return dist_matrix

    # Solve TSP for a given combination of points
    def solve_tsp(points):
        dist_matrix = build_distance_matrix([entry] + list(points))
        num_points = len(points) + 1  # Include entry point
        min_steps = float('inf')

        # Permutations of visiting all targets starting and ending at entry
        for perm in permutations(range(1, num_points)):
            steps = dist_matrix[(0, perm[0])]  # Entry to first target
            for i in range(len(perm) - 1):
                steps += dist_matrix[(perm[i], perm[i + 1])]
            steps += dist_matrix[(perm[-1], 0)]  # Last target back to entry
            min_steps = min(min_steps, steps)

        return min_steps

    # Evaluate all combinations of one of each target
    min_steps = float('inf')
    best_combination = None
    for combination in all_combinations:
        steps = solve_tsp(combination)
        if steps < min_steps:
            min_steps = steps
            best_combination = combination

    if min_steps == float('inf'):
        return -1, maze  # No valid path found

    # Mark the path in the maze
    def mark_path(start, end):
        distances = bfs(start)
        path = []
        current = end
        while current != start:
            path.append(current)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = current[0] + dx, current[1] + dy
                if (nx, ny) in distances and distances[(nx, ny)] == distances[current] - 1:
                    current = (nx, ny)
                    break
        for x, y in path:
            if maze[x][y] == '.':
                maze[x][y] = '*'

    # Mark the paths in the maze based on the best combination
    current_point = entry
    for point in best_combination:
        mark_path(current_point, point)
        current_point = point
    mark_path(current_point, entry)  # Return to entry

    return min_steps, maze

# Example maze
maze = [
    "##########.##########",
    "#...................#",
    "#.###.##.###.##.#.#.#",
    "#..A#.#..~~~....#A#.#",
    "#.#...#.~~~~~...#.#.#",
    "#.#.#.#.~~~~~.#.#.#.#",
    "#...#.#.B~~~B.#.#...#",
    "#...#....BBB..#....##",
    "#C............#....C#",
    "#####################"
]

# Convert to list of lists for easier manipulation
maze = [list(row) for row in f]

# Find the shortest round trip
result, updated_maze = find_shortest_collect_all_any_order(maze)

print("Shortest round trip distance: part 2 -", result)
print("Updated maze:")
for row in updated_maze:
    print("".join(row))
