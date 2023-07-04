#!/usr/bin/python3
"""

Prints a square with the character '#'
of any positive integer size.

"""


def print_square(size):
    """
    Prints a square of a given size using the character '#'.

    Args:
        size (int): The length of the square's sides.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.

    Returns:
        None
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(1, size + 1):
        for y in range(1, size + 1):
            print('#', end='')

            if y % size == 0 and y > 0:
                print()
