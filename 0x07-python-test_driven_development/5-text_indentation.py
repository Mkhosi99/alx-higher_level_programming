#!/usr/bin/python3
"""Module defines a text-indentation function."""


def text_indentation(text):
    """Prints text with two new lines after each of these chars '.' , '?', ':'

    Args:
        text (string): The text to be printed.
    Raises:
        TypeError: If text input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = 0
    while s < len(text) and text[s] == ' ':
        s += 1

    while s < len(text):
        print(text[s], end="")
        if text[s] == "\n" or text[s] in ".?:":
            if text[s] in ".?:":
                print("\n")
            s += 1
            while s < len(text) and text[s] == ' ':
                s += 1
            continue
        s += 1
