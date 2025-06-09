def matrix_islands_with_diagonals_solution(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    island_count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    def dfs(r, c):
        visited[r][c] = True
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                not visited[nr][nc] and matrix[nr][nc] == 1):
                dfs(nr, nc)

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and not visited[r][c]:
                island_count += 1
                dfs(r, c)

    return island_count


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(cell) for cell in row))


def run_matrix_island_diagonal_tests():
    test_cases = [
        [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]],

        [[1, 1, 0],
         [0, 1, 0],
         [0, 0, 1]],

        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],

        [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]],

        [[1, 0, 1],
         [0, 0, 0],
         [1, 0, 1]]
    ]

    for i, matrix in enumerate(test_cases, 1):
        print(f"Matrix {i}:")
        print_matrix(matrix)
        result = matrix_islands_with_diagonals_solution(matrix)
        print(f"Number of islands (with diagonals): {result}\n")

run_matrix_island_diagonal_tests()
