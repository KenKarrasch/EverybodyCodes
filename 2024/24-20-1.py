g = open('24-20-1.txt').read().split('\n')

ng = []
for i in g:
    lst = []
    for j in i:
        lst.append(j)
    ng.append(lst)

    #directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  
print(ng)


import heapq

def max_score(grid, moves=100):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # Up, Down, Left, Right

    # Find the starting position 'S'
    start = None
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 'S':
                start = (x, y)
                break
        if start:
            break

    if not start:
        raise ValueError("Starting position 'S' not found on the map")

    start_x, start_y = start

    # Step 1: Find all 2x2 sub-grids that are filled with '+'
    best_score = float('-inf')
    best_path = []
    target_positions = []
    
    for i in range(rows - 1):
        for j in range(cols - 1):
            if (grid[i][j] == '+' and grid[i][j + 1] == '+' and
                grid[i + 1][j] == '+' and grid[i + 1][j + 1] == '+'):
                target_positions.append((i, j))

    # Step 2: Use a modified BFS/DFS to find the path to any of these target positions
    max_heap = [(-0, start_x, start_y, moves, 1, [(start_x, start_y)])]
    visited = {}
    dp = {}

    while max_heap:
        current_score, x, y, remaining_moves, current_dir, path = heapq.heappop(max_heap)
        current_score = -current_score

        if current_score > best_score:
            best_score = current_score
            best_path = path

        if remaining_moves == 0:
            continue

        if (x, y, current_dir, remaining_moves) in dp and dp[(x, y, current_dir, remaining_moves)] >= current_score:
            continue
        dp[(x, y, current_dir, remaining_moves)] = current_score

        # Generate valid moves: left, forward, right
        for turn in [-1, 0, 1]:  # Left, Forward, Right
            if current_dir == -1 and turn != 0:
                continue  # No direction initially, only move forward
            new_dir = (current_dir + turn) % 4 if current_dir != -1 else 0

            if current_dir != -1 and (current_dir + 2) % 4 == new_dir:
                continue  # Skip reversing direction

            dx, dy = directions[new_dir]
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
                cell_score = 1 if grid[nx][ny] == '+' else -2 if grid[nx][ny] == '-' else -1
                new_score = current_score + cell_score

                # Push the new state into the heap
                heapq.heappush(max_heap, (-new_score, nx, ny, remaining_moves - 1, new_dir, path + [(nx, ny)]))

    # Step 3: Visualize the best path on the grid
    final_map = [list(row) for row in grid]
    for idx, (px, py) in enumerate(best_path):
        if idx > 0:  # Skip marking the starting position
            final_map[px][py] = '*'

    # Print the final map
    for row in final_map:
        print(" ".join(row))
    print(f"Maximum score: {best_score}")

    return best_score

# Example usage
grid = [
    ['S', '+', '.', '+'],
    ['-', '#', '-', '.'],
    ['.', '-', '+', '+'],
    ['+', '+', '.', '#']
]

print("Maximum score:", 1000 + max_score(ng, moves=100))
