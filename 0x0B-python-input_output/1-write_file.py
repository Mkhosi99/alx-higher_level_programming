#!/usr/bin/python3

"""Define a file-writing function."""


def write_file(filename="", text=""):
    """Function writes a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written in text.
    """
    with open(filename, "w", encoding="utf-8") as fle:
        return fle.write(text)
