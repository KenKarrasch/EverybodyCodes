import heapq

#  37 on the global leaderboard. part 3 - 4m 16s solve

def find_cheapest_route_with_path(grid):
    rows, cols = len(grid), len(grid[0])

    # Parse grid, find all 'S' points and the 'E' point, and prepare numeric grid
    start_points = []
    end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_points.append((r, c))
                grid[r][c] = '0'  # Replace 'S' with '0'
            elif grid[r][c] == 'E':
                end = (r, c)
                grid[r][c] = '0'  # Replace 'E' with '0'

    # Convert grid to integers where '#' and ' ' are walls (-1)
    numeric_grid = [
        [int(char) if char not in ['#', ' '] else -1 for char in row]
        for row in grid
    ]

    # Priority queue for Dijkstra's (min-heap)
    pq = [(0, r, c) for r, c in start_points]  # Initialize with all start points
    visited = set()
    parent = {}  # To store the path

    # Dijkstra's loop
    while pq:
        cost, x, y = heapq.heappop(pq)

        # If we've reached the end, reconstruct the path
        if (x, y) == end:
            path = []
            while (x, y) in parent:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start_points[0])  # One of the 'S' points
            return cost, path[::-1]  # Reverse path for correct order

        # Skip already visited nodes
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Check neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            # Validity checks
            if 0 <= nx < rows and 0 <= ny < cols and numeric_grid[nx][ny] != -1:
                current = numeric_grid[x][y]
                neighbor = numeric_grid[nx][ny]

                # Calculate wrap-around cost
                if current > neighbor:  # Downward wrap-around
                    diff = min(abs(current - neighbor), 10 - current + neighbor)
                elif neighbor > current:  # Upward wrap-around
                    diff = min(abs(neighbor - current), 10 - neighbor + current)
                else:  # No wrap-around
                    diff = abs(neighbor - current)

                step_cost = diff + 1
                if (nx, ny) not in visited:
                    heapq.heappush(pq, (cost + step_cost, nx, ny))
                    parent[(nx, ny)] = (x, y)  # Store the path

    return -1, []  # Return -1 if no path exists

def draw_path_on_grid(grid, path):
    # Convert grid (list of strings) into a mutable list of lists
    grid_with_path = [list(row) for row in grid]

    for r, c in path:
        if grid_with_path[r][c] not in ['S', 'E']:  # Don't overwrite start/end
            grid_with_path[r][c] = '*'

    # Convert grid back to a string format for display
    return '\n'.join(''.join(row) for row in grid_with_path)

# Example usage
text_file_lines = [
    "S1 3",
    "45 S",
    "78  E",
]

f = open('24-13-3.txt').read().split('\n')

# Convert text file lines to a list of lists for processing
grid = [list(line) for line in f]
cost, path = find_cheapest_route_with_path(grid)
if cost != -1:
    print(f"Cheapest cost: {cost}")
    print("Path:")
    print(draw_path_on_grid(f, path))
else:
    print("No path found!")
