#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    class Square that defines a square by: (based on 5-square.py)

    Attributes:
        __size (int, optional): Private instance attribute representing
        the size of the square.

        __position (tuple, optional): Private instance attribute representing
        the position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): Size of the square. Default to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size
        self.__position = position

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
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Retrieves position

        Returns:
            tuple: tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square

        Args:
            value (tuple): The position of the square

        Raises:
            TypeError: If tuple is not two positive integer

        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of"
                                " 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #
        And sets position

        Prints an empty line if size is 0
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
