#!/usr/bin/python3
import sys

def init_board(n):
    return [[' ' for _ in range(n)] for _ in range(n)]

def get_solution(board):
    solution = []
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 'Q':
                solution.append([r, c])
    return solution

def is_safe(board, row, col):
    n = len(board)
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_nqueens(board, row, solutions):
    n = len(board)
    if row == n:
        solutions.append(get_solution(board))
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            solve_nqueens(board, row + 1, solutions)
            board[row][col] = ' '

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(N)
    solutions = []
    solve_nqueens(board, 0, solutions)
    for sol in solutions:
        print(sol)

