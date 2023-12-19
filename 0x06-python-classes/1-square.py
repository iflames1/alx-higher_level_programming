#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    class Square that defines a square by: (based on 1-square.py)

    Attributes:
        size: Private instance attribute representing the size of the square.
    """
    def __init__(self, size):
        """
        Args:
            size: Size of the square.
        """
        self.__size = size
