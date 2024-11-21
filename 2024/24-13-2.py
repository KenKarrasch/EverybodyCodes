f = open('24-13-1.txt').read().split('\n')

# Same as part 1, just a bigger map. 53 on the global leaderboard, 45s solve.

import heapq

def find_cheapest_route(grid):
    rows, cols = len(grid), len(grid[0])

    # Parse grid, find 'S' and 'E', and prepare numeric grid
    start = end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
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
    pq = [(0, start[0], start[1])]  # (cost, row, col)
    visited = set()

    # Dijkstra's loop
    while pq:
        cost, x, y = heapq.heappop(pq)

        # If we've reached the end, return the total cost
        if (x, y) == end:
            return cost

        # Skip already visited nodes
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Check neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            # Validity checks
            if 0 <= nx < rows and 0 <= ny < cols and numeric_grid[nx][ny] != -1:
                # Calculate cost: step cost + numeric difference
                if numeric_grid[x][y] == 9 and numeric_grid[nx][ny] == 0:
                    diff = 2  # Wrap-around 9 -> 0
                elif numeric_grid[x][y] == 0 and numeric_grid[nx][ny] == 9:
                    diff = 2  # Wrap-around 0 -> 9
                else:
                    diff = abs(numeric_grid[nx][ny] - numeric_grid[x][y])

                step_cost = diff + 1
                heapq.heappush(pq, (cost + step_cost, nx, ny))

    return -1  # Return -1 if no path exists

# Example usage
text_file_lines = [
    "S1 3",
    "45  ",
    "78  E",
]

grid = [list(line) for line in f]
print(find_cheapest_route(grid))


