#!/usr/bin/python3
"""Module defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Function prints a name.

    Args:
        first_name (str): Indicates the first name.
        last_name (str): Indicates the last name.
    Raises:
        TypeError: If first_name and last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
