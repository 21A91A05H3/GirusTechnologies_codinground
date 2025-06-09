from collections import deque

def shortest_path_with_teleport(grid):
    n, m = len(grid), len(grid[0])
    if grid[0][0] != '.' or grid[n-1][m-1] != '.':
        return -1
    empty = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == '.']
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((0, 0, 0, False))
    visited[0][0][0] = True
    while queue:
        x, y, steps, teleported = queue.popleft()
        if (x, y) == (n-1, m-1):
            return steps
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.':
                if not visited[nx][ny][teleported]:
                    visited[nx][ny][teleported] = True
                    queue.append((nx, ny, steps+1, teleported))
        if not teleported:
            for ex, ey in empty:
                if (ex, ey) != (x, y) and not visited[ex][ey][1]:
                    visited[ex][ey][1] = True
                    queue.append((ex, ey, steps+1, True))
    return -1

def display_grid_and_result(grid):
    print("Input grid:")
    for row in grid:
        print(' '.join(row))
    print("Output:", shortest_path_with_teleport(grid))
    print()

grid1 = [
    ['.','.','#','.'],
    ['#','.','#','.'],
    ['.','.','.','#'],
    ['#','#','.','.']
]

grid2 = [
    ['.','#','#','.'],
    ['.','.','#','#'],
    ['#','.','.','.'],
    ['#','#','#','.']
]

display_grid_and_result(grid1)
display_grid_and_result(grid2)
