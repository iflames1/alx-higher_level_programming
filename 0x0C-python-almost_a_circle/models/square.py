#!/usr/bin/python3

"""This module defines the Square class, a subclass of Rectangle, representing
a geometric square.

The Square class inherits from the Rectangle class and adds attributes and
methods specific to squares.

Attributes:
    id (int): A unique identifier for the square.
    size (int): The size of the square.
    x (int): The x-coordinate of the top-left corner of the square.
    y (int): The y-coordinate of the top-left corner of the square.

Methods:
    __init__(self, size, x=0, y=0, id=None): Initializes a new instance of the
    Square class.

    size (int): The size of the square.

    size (int): The size of the square.

    update(self, *args, **kwargs): Updates the attributes of the square using
    either positional or keyword arguments.

    to_dictionary(self): Converts the square attributes to a dictionary.

    __str__(self): Returns a string representation of the square.

Usage:
    Example usage of creating and manipulating a square:
        >>> s = Square(5, 10, 15)
        >>> print(s.size)
        5
        >>> s.size = 8
        >>> print(s.area())
        64
        >>> s.display()
                   ########
                   ########
                   ########
                   ########
                   ########
                   ########
                   ########
                   ########
        >>> s.update(1, 3, 4, 2)
        >>> print(s.to_dictionary())
        {'id': 1, 'size': 3, 'x': 4, 'y': 2}
        >>> print(s)
        [Square] (1) 4/2 - 3
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the top-left corner of the square.
            y (int): The y-coordinate of the top-left corner of the square.
            id (int): A unique identifier for the square. If None, a unique ID
            is assigned.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a positive integer.
        """
        self.validate_integer("size", value)
        self.validate_positive("size", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the square using either positional or
        keyword arguments.

        Args:
            *args: Positional arguments to update the attributes in the order
            (id, size, x, y).
            **kwargs: Keyword arguments to update the attributes using
            attribute names.

        Example:
            s.update(1, 5, 10, 2)  # Updates id=1, size=5, x=10, y=2
            s.update(size=8)  # Updates size=8
        """
        if args:
            attr_names = ["id", "size", 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Converts the square attributes to a dictionary.

        Returns:
            dict: A dictionary representation of the square attributes.
        """
        return {
            "id": self.id,
            "size": self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
