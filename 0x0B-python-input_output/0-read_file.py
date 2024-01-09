#!/usr/bin/python3

"""Define a text file-reading function"""


def read_file(filename=""):
    """Print text of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as fle:
        print(fle.read(), end="")
