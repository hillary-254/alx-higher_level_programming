#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """_summary_

    Args:
        BaseGeometry (_type_): _description_

    Methods:
        __init__(self, width, height): Initializes a Rectangle instance
        with the given width and height.
        area(self): Calculates and returns the area of the rectangle.
        __str__(self): Returns a string representation of the rectangle
        in the format [Rectangle] <width>/<height>.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle in the
            format [Rectangle] <width>/<height>.
        """
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
