#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""

import sys


def initialize_board(size):
    """Initialize an `size`x`size` sized chessboard with empty cells."""
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return board


def deepcopy_board(board):
    """Return a deep copy of a chessboard."""
    if isinstance(board, list):
        return [deepcopy_board(row) for row in board]
    return board


def extract_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    res = [[r, c] for r, row in enumerate(board) for c, cell in enumerate(row) if cell == 'Q']
    return res


def mark_attacked_spots(board, row, col):
    """Mark spots on a chessboard where queens can no longer be placed."""
    for c in range(col + 1, len(board)):
        board[row][c] = 'x'  # Mark forward spots
    for c in range(col - 1, -1, -1):
        board[row][c] = 'x'  # Mark backward spots
    for r in range(row + 1, len(board)):
        board[r][col] = 'x'  # Mark spots below
    for r in range(row - 1, -1, -1):
        board[r][col] = 'x'  # Mark spots above
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = 'x'  # Mark diagonally down to the right
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = 'x'  # Mark diagonally up to the left
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = 'x'  # Mark diagonally up to the right
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = 'x'  # Mark diagonally down to the left
        c -= 1


def recursive_nqueens(board, current_row, placed_queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        current_row (int): The current working row.
        placed_queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if placed_queens == len(board):
        solutions.append(extract_solution(board))
        return solutions

    for col in range(len(board)):
        if board[current_row][col] == ' ':
            tmp_board = deepcopy_board(board)
            tmp_board[current_row][col] = 'Q'
            mark_attacked_spots(tmp_board, current_row, col)
            solutions = recursive_nqueens(tmp_board, current_row + 1, placed_queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_board(int(sys.argv[1]))
    solution_set = recursive_nqueens(chessboard, 0, 0, [])
    for solution in solution_set:
        print(solution)
