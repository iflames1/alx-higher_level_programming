#!/usr/bin/python3
""" defines a rectangle class based on 5-rectangle.py. """


class Rectangle:
    """ class that defines a rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Args:
            self:

        Returns (int): area of rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Args:
            self:

        Returns: perimeter of rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Prints the rectangle using '#' characters.
        Returns:
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """ Returns: Returns a string representation of the rectangle. """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Prints the message when an instance is deleted. """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
