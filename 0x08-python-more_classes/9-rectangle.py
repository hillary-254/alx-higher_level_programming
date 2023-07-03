#!/usr/bin/python3
"""
Rectangle Module
"""


class Rectangle:
    """
    Class representing a rectangle.

    Attributes:
        number_of_instances (int): The number of rectangle instances.
        print_symbol (str): The symbol used to represent the rectangle when printed.

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

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

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle.

        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for _ in range(self.__height):
            rect_str += str(self.print_symbol) * self.__width + "\n"
        return rect_str.rstrip()

    def __repr__(self):
        """
        Return a string representation of the rectangle for debugging.

        Returns:
            str: A string representing the rectangle.

        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Perform cleanup when the rectangle instance is deleted.

        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the one with the bigger or equal area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle with the bigger or equal area.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a square rectangle with the given size.

        Args:
            size (int, optional): The size of the square rectangle. Defaults to 0.

        Returns:
            Rectangle: A square rectangle with equal width and height.

        """
        return cls(size, size)
