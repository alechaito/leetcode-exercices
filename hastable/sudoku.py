from math import ceil, floor

"""board = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]
]"""

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

def isValidSudoku(board) -> bool:
    row = set()
    col = set()
    grid = set()
    rows = len(board)
    cols = len(board[0])

    for i in range(rows):
        for j in range(cols):
            if board[i][j] != ".":
                # it has already a row with this number
                if (i, board[i][j]) in row:
                    return False 
                # it has already a col with this number
                if (j, board[i][j]) in col:
                    return False 
                if (i//3, j//3, board[i][j]) in grid:
                    return False
                # add to hash row_col
                row.add((i, board[i][j]))
                # add to hash row_col
                col.add((j, board[i][j]))
                # add to hash grid
                grid.add((i//3, j//3, board[i][j]))
            
    return True

isValidSudoku(board)