#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""module with class BaseGeometry"""


class Square(Rectangle):
    """
    A class representing a square.

    This class inherits from the Rectangle class and provides functionality specific to squares.

    Methods:
        __init__(self, size): Initializes a Square instance with
        the given size.
        area(self): Calculates and returns the area of the square.
        __str__(self): Returns a string representation of the square in the 
        format [Square] <size>/<size>.

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

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string representation of the square in the format [Square] <size>/<size>.

        """
        return "[Square] {}/{}".format(self.__size, self.__size)
