#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    class Square that defines a square by: (based on 2-square.py)

    Attributes:
        __size (int): Private instance attribute representing
        the size of the square.
        area: Public instance attribute representing the area of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): Size of the square. Default to 0.

        Raises:
             TypeError: If size is not an integer.
             ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
