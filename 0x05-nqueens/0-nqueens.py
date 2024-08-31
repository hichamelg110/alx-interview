#!/usr/bin/python3
"""
solution to the N Queens problem
"""
import sys

def solve_recursively(row, size, columns, positive_diag, negative_diag, chess_board):
    """
    Recursive function to find solutions
    """
    if row == size:
        solution = []
        for i in range(len(chess_board)):
            for j in range(len(chess_board[i])):
                if chess_board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    for col in range(size):
        if col in columns or (row + col) in positive_diag or (row - col) in negative_diag:
            continue

        columns.add(col)
        positive_diag.add(row + col)
        negative_diag.add(row - col)
        chess_board[row][col] = 1

        solve_recursively(row + 1, size, columns, positive_diag, negative_diag, chess_board)

        columns.remove(col)
        positive_diag.remove(row + col)
        negative_diag.remove(row - col)
        chess_board[row][col] = 0

def solve_nqueens(size):
    """
    Solution to N Queens problem
    Args:
        size (int): number of queens. Must be >= 4
    Return:
        Prints lists representing coordinates of each
        queen for all possible solutions
    """
    columns = set()
    positive_diagonals = set()
    negative_diagonals = set()
    chess_board = [[0] * size for _ in range(size)]

    solve_recursively(0, size, columns, positive_diagonals, negative_diagonals, chess_board)

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(args[1])
        if board_size < 4:
            print("N must be at least 4")
            sys.exit(1)
        solve_nqueens(board_size)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
