#!/usr/bin/python3

import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with ' '."""
    return [[' ' for _ in range(n)] for _ in range(n)]

def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    return [row[:] for row in board]

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    return [[r, board[r].index('Q')] for r in range(len(board))]

def xout(board, row, col):
    """X out spots on a chessboard where queens attack."""
    n = len(board)
    for c in range(col + 1, n):
        board[row][c] = 'x'
    for c in range(col - 1, -1, -1):
        board[row][c] = 'x'
    for r in range(row + 1, n):
        board[r][col] = 'x'
    for r in range(row - 1, -1, -1):
        board[r][col] = 'x'
    c = col + 1
    for r in range(row + 1, n):
        if c >= n:
            break
        board[r][c] = 'x'
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = 'x'
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= n:
            break
        board[r][c] = 'x'
        c += 1
    c = col - 1
    for r in range(row + 1, n):
        if c < 0:
            break
        board[r][c] = 'x'
        c -= 1

def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == ' ':
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = 'Q'
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(N)
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)

