#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    class Square that defines a square by: (based on 2-square.py)

    Attributes:
        __size (int): Private instance attribute representing
        the size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): Size of the square. Default to 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Gets the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square
        Args:
            value (int): The size to set.

        Raises:
             TypeError: If size is not an integer.
             ValueError: If size is less than 0.
        Returns:

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
