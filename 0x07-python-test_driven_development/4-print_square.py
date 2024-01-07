#!/usr/bin/python3
"""Module defines a function that prints a square."""


def print_square(size):
    """Functios prints a square with the # character.

    Args:
        size (int): Height and width of the square.
    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
