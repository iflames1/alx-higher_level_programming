#!/usr/bin/python3

"""This module defines the Rectangle class, a subclass of Base, representing a
geometric rectangle.

The Rectangle class inherits from the Base class and adds attributes and
methods specific to rectangles.

Attributes:
    id (int): A unique identifier for the rectangle.
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    x (int): The x-coordinate of the top-left corner of the rectangle.
    y (int): The y-coordinate of the top-left corner of the rectangle.

Methods:
    __init__(self, width, height, x=0, y=0, id=None): Initializes a new
    instance of the Rectangle class.

    validate_integer(self, attr_name, value): Validates if the value is an
    integer.

    validate_positive(self, attr_name, value): Validates if the value is a
    positive integer.

    validate_non_negative(self, attr_name, value): Validates if the value is a
    non-negative integer.

    area(self): Calculates and returns the area of the rectangle.

    display(self): Displays the rectangle using '#' characters.

    update(self, *args, **kwargs): Updates the attributes of the rectangle
    using either positional or keyword arguments.

    to_dictionary(self): Converts the rectangle attributes to a dictionary.

    __str__(self): Returns a string representation of the rectangle.

Usage:
    Example usage of creating and manipulating a rectangle:
        >>> r = Rectangle(10, 20, 30, 40)
        >>> print(r.area())
        200
        >>> r.display()
           ##########
           ##########
           ##########
           ##########
           ##########
        >>> r.update(width=5, height=5, x=0, y=0)
        >>> print(r.to_dictionary())
        {'id': 1, 'width': 5, 'height': 5, 'x': 0, 'y': 0}
        >>> print(r)
        [Rectangle] (1) 0/0 - 5/5
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the top-left corner of the rectangle.
            y (int): The y-coordinate of the top-left corner of the rectangle.
            id (int): A unique identifier for the rectangle. If None, a unique
            ID is assigned.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a positive integer.
        """
        self.validate_integer("width", value)
        self.validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a positive integer.
        """
        self.validate_integer("height", value)
        self.validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """int: The x-coordinate of the top-left corner of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the top-left corner of the rectangle.

        Args:
            value (int): The x-coordinate of the top-left corner of the
            rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a non-negative integer.
        """
        self.validate_integer("x", value)
        self.validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """int: The y-coordinate of the top-left corner of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the top-left corner of the rectangle.

        Args:
            value (int): The y-coordinate of the top-left corner of the
            rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a non-negative integer.
        """
        self.validate_integer("y", value)
        self.validate_non_negative("y", value)
        self.__y = value

    def validate_integer(self, attr_name, value):
        """Validates if the value is an integer.

        Args:
            attr_name (str): The name of the attribute being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")

    def validate_positive(self, attr_name, value):
        """Validates if the value is a positive integer.

        Args:
            attr_name (str): The name of the attribute being validated.
            value: The value to be validated.

        Raises:
            ValueError: If the value is not a positive integer.
        """
        if value <= 0:
            raise ValueError(f"{attr_name} must be > 0")

    def validate_non_negative(self, attr_name, value):
        """Validates if the value is a non-negative integer.

        Args:
            attr_name (str): The name of the attribute being validated.
            value: The value to be validated.

        Raises:
            ValueError: If the value is not a non-negative integer.
        """
        if value < 0:
            raise ValueError(f"{attr_name} must be >= 0")

    def area(self):
        """Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """Displays the rectangle using '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle using either positional or
        keyword arguments.

        Args:
            *args: Positional arguments to update the attributes in the order
            (id, width, height, x, y).
            **kwargs: Keyword arguments to update the attributes using
            attribute names.

        Example:
            r.update(1, 5, 10, 2, 3)  # Updates id=1, width=5, height=10, x=2,
            y=3
            r.update(width=8, height=8)  # Updates width=8, height=8
        """
        if args:
            attr_names = ["id", "width", "height", 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Converts the rectangle attributes to a dictionary.

        Returns:
            dict: A dictionary representation of the rectangle attributes.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")
