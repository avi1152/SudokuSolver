import numpy as np

def Show(_board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(board[0])):
            if (j+1) % 3 == 0 and j != 8:
                print(_board[i][j], end=" | ")
            else:
                print(_board[i][j], end=" ")
        print()

def EmptyCell(_board):
    for i in range(9):
        for j in range(9):
            if _board[i][j] == 0:
                return i, j
    return None

def IsValid(_element, _row, _col, _board):
    rq = _row // 3
    cq = _col // 3
    grid = _board[rq*3:rq*3+3, cq*3:cq*3+3]
    if _element in _board[_row] or _element in _board[:, _col] or _element in grid:
        return False
    return True

def Solve(_board):
    emptyCell = EmptyCell(_board)

    if emptyCell is None:
        return _board
    else:
        row, col = emptyCell
        for i in range(1, 10):
            if IsValid(i, row, col, _board):
                _board[row][col] = i

                if Solve(_board) is not None:
                    return _board

                _board[row][col] = 0

    return None

board = [
    [8, 2, 7, 1, 5, 4, 3, 9, 6],
    [0, 6, 5, 3, 2, 0, 1, 4, 8],
    [3, 4, 1, 6, 8, 9, 7, 5, 2],
    [5, 9, 3, 0, 6, 8, 2, 7, 1],
    [4, 7, 0, 5, 1, 3, 6, 8, 9],
    [6, 1, 8, 9, 7, 2, 4, 3, 0],
    [7, 8, 6, 2, 3, 5, 9, 1, 4],
    [1, 5, 4, 7, 0, 6, 8, 2, 3],
    [2, 0, 9, 8, 4, 1, 5, 6, 7]
]
board = np.array(board)

Show(Solve(board))
