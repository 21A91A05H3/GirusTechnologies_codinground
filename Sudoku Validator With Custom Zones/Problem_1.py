def is_valid_group(group):
    nums = [cell for cell in group if cell != "."]
    return len(nums) == len(set(nums)) and all(cell in "123456789" for cell in nums)
def validate_rows(board):
    for row in board:
        if not is_valid_group(row):
            return False
    return True
def validate_columns(board):
    for col in zip(*board):
        if not is_valid_group(col):
            return False
    return True
def validate_boxes(board):
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [board[r][c] for r in range(box_row, box_row + 3)
                                 for c in range(box_col, box_col + 3)]
            if not is_valid_group(box):
                return False
    return True
def validate_custom_zones(board, custom_zones):
    for zone in custom_zones:
        cells = [board[r][c] for r, c in zone]
        if not is_valid_group(cells):
            return False
    return True
def is_valid_sudoku(board, custom_zones):
    return (
        validate_rows(board)
        and validate_columns(board)
        and validate_boxes(board)
        and validate_custom_zones(board, custom_zones)
    )
def run_tests():
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    custom_zones = [
        [(0, 0), (0, 1), (1, 0), (1, 1), (2, 1), (2, 2), (4, 1), (4, 2), (4, 0)],  
        [(8, 8), (7, 8), (6, 8), (8, 7), (7, 7), (6, 7), (8, 6), (7, 6), (6, 6)]
    ]

    print("Test 1 - Valid board and zones:", is_valid_sudoku(board, custom_zones))

    board[2][2] = "6"
    print("Test 2 - Invalid custom zone:", is_valid_sudoku(board, custom_zones))
    board[2][2] = "8"

    board[0][1] = "5"  
    print("Test 3 - Invalid row:", is_valid_sudoku(board, custom_zones))  

    board[0][1] = "3"

    board[1][1] = "3"  
    print("Test 4 - Invalid box:", is_valid_sudoku(board, custom_zones))  

run_tests()
