#!/usr/bin/python3
""" defines a rectangle class based on 0-rectangle.py. """


class Rectangle:
    """ class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns: Private instance for width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width for rectangle.
        Args:
            value (int):
        Raises:
             TypeError: if value is not an integer.
             ValueError: if value is less than 0

        Returns (int): private instance for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height for rectangle.
        Args:
            value (int):
        Raises:
             TypeError: if value is not an integer.
             ValueError: if value is less than 0

        Returns (int): private instance for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
