#!/usr/bin/python3
"""
Class defining a square.
"""


class Square:
    """
    Defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not a number (float or integer).
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Equality comparison between two squares based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the squares have equal areas, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparison between two squares based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the squares have unequal areas, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparison between two squares based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the current square is less
            than the other square, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal to comparison between two squares
        based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the current square is less than
            or equal to the other square, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparison between two squares based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the current square is greater
            than the other square, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal to comparison between two
        squares based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the current square is greater than or
            equal to the other square, False otherwise.
        """
        return self.area() >= other.area()
