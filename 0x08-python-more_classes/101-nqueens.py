#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_board(queens):
    for queen in queens:
        print(queen, end=" ")
    print()


def solve_nqueens(board, col, N, queens):
    if col == N:
        print_board(queens)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            queens.append([i, col])
            solve_nqueens(board, col + 1, N, queens)
            board[i][col] = 0
            queens.pop()


def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    queens = []
    solve_nqueens(board, 0, N, queens)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
