#!/usr/bin/python3
import sys

def init_board(n):
    return [[' ' for _ in range(n)] for _ in range(n)]

def get_solution(board):
    return [[r, board[r].index("Q")] for r in range(len(board))]

def xout(board, row, col):
    n = len(board)
    for i in range(n):
        board[row][i] = "x"
        board[i][col] = "x"
        if row + i < n and col + i < n:
            board[row + i][col + i] = "x"
        if row - i >= 0 and col - i >= 0:
            board[row - i][col - i] = "x"
        if row + i < n and col - i >= 0:
            board[row + i][col - i] = "x"
        if row - i >= 0 and col + i < n:
            board[row - i][col + i] = "x"

def recursive_solve(board, row, queens, solutions):
    if queens == len(board):
        solutions.append(get_solution(board))
        return

    for col in range(len(board)):
        if board[row][col] == " ":
            tmp_board = [row[:] for row in board]
            tmp_board[row][col] = "Q"
            xout(tmp_board, row, col)
            recursive_solve(tmp_board, row + 1, queens + 1, solutions)

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
    recursive_solve(board, 0, 0, solutions)
    for sol in solutions:
        print(sol)

