#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""module with class BaseGeometry"""


class Square(Rectangle):
    """
    A class representing a square.
    """
    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.

        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string representation of the square in the
            format [Square] <size>/<size>.

        """
        return "[Square] {}/{}".format(self.__size, self.__size)
