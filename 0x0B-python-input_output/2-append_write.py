#!/usr/bin/python3
"""Module that appends strings at end of a text file"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and
    returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        Defaults to an empty string.
        text (str): The string to be appended to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
