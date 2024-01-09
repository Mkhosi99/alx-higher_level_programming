#!/usr/bin/python3

"""Define a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of ints representing the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        triang = triangle[-1]
        temp = [1]
        for x in range(len(triang) - 1):
            temp.append(triang[x] + triang[x + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
