#!/usr/bin/python3

""" N queens """

import sys


def is_safe(board, row, col, n):
    """ It checks if it's a safe to place a queen at board[row][col] """
    # Checks the row on the left side.
    for x in range(col):
        if board[row][x] == 1:
            return False

    # Checks upper diagonal on the left side.
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    # Checks lower diagonal on the left side.
    for x, y in zip(range(row, n), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n, solutions):
    """ Utility func to solve N queens problem """
    # If all queens are placed then return True.
    if col >= n:
        solution = []
        for x in range(n):
            for y in range(n):
                if board[x][y] == 1:
                    solution.append([x, y])
        solutions.append(solution)
        return

    # Considering this column & try placing this queen in all rows one by one.
    for x in range(n):
        if is_safe(board, x, col, n):
            board[x][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[x][col] = 0


def solve_nqueens(n):
    """ Solve the N queens problem set """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    solve_nqueens_util(board, 0, n, solutions)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
