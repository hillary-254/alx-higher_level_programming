#!/usr/bin/python3
"""
Rectangle Module
"""


class Rectangle:
    """
    A class that represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        self.__check_valid_width(value)
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        self.__check_valid_height(value)
        self.__height = value

    def __check_valid_width(self, width):
        """
        Check if the width is a valid integer.

        Args:
            width (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    def __check_valid_height(self, height):
        """
        Check if the height is a valid integer.

        Args:
            height (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __draw_rectangle(self):
        """
        Draw the rectangle with their size.

        Returns:
            str: An empty string if width or height is 0,
            otherwise returns a string with the rectangle.
        """
        rect_str = ""
        w = self.__width
        h = self.__height

        if w == 0 or h == 0:
            return rect_str

        for i in range(h):
            for j in range(w):
                rect_str += "#"

            if i != h - 1:
                rect_str += "\n"

        return rect_str

    def __str__(self):
        """
        Get the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return self.__draw_rectangle()

    def __repr__(self):
        """
        Get the string representation of the rectangle for eval().

        Returns:
            str: The string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"
