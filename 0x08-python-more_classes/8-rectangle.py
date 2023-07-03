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
        number_of_instances (int): The number of instances of the Rectangle class.
        print_symbol (str): The symbol used for string representation of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle object.

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
        Getter method for the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If the width value is not an integer.
            ValueError: If the width value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If the height value is not an integer.
            ValueError: If the height value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 0 if self.__width == 0 or self.__height == 0 else 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The rectangle represented as a string of print_symbol characters.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for _ in range(self.__height):
            rect_str += str(self.print_symbol) * self.__width + "\n"
        return rect_str.rstrip()

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be used to recreate the object.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Deletes the rectangle object, decrements the number of instances, and prints a farewell message.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with the bigger or equal area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the bigger or equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
