#!/usr/bin/python3
"""
A function that adds 2 intergers/ float is defined
"""


def add_integer(a, b=98):
    """Addition of function a and b should be returned

    A float will be typecasted into an interger before addition is performed

    Raises:
        TypeError: If a or b is not an integer and not a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
