def read_grid_from_file(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid


def dfs(grid, x, y, visited):
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        cx, cy = stack.pop()
        # Explore the four possible directions (up, down, left, right)
        for nx, ny in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]:
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == '1':
                visited[nx][ny] = True
                stack.append((nx, ny))


def count_connected_shapes(grid):
    if not grid:
        return 0

    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and not visited[i][j]:
                dfs(grid, i, j, visited)
                count += 1

    return count


if __name__ == "__main__":
    file_path = 'data_large.txt'
    grid = read_grid_from_file(file_path)
    num_shapes = count_connected_shapes(grid)
    print(f"Number of connected shapes: {num_shapes}")
