#!/usr/bin/python3
"""Module that reads then prints a text file"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to be read.
        Defaults to an empty string.

    Returns:
        None
    """
    with open(filename) as f:
        text = f.read()
        print(text, end="")
