#!/usr/bin/python3
"""Defining a matrix division function."""


def matrix_divided(matrix, div):
    """Function divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers/floats.
        div (int/float): Indicates the divisor.
    Raises:
        TypeError: If the matrix has no integers/float.
        TypeError: If the matrix has rows of different sizes.
        TypeError: If div is not an integer or a float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix that represents the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(line, list) for line in matrix) or
        not all((isinstance(elem, int) or isinstance(elem, float))
                for elem in [numb for line in matrix for numb in line])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(line) == len(matrix[0]) for line in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), line)) for line in matrix])
