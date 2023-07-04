#!/usr/bin/python3
"""

This module prints first and last name

"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format "My name is <first_name> <last_name>" or "My name is <first_name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
