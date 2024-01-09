#!/usr/bin/python3

"""Define a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): Name of the file to append.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as fle:
        return fle.write(text)
