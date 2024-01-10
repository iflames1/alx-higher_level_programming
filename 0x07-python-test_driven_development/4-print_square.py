#!/usr/bin/python3
""" module for print_square method """


def print_square(size):
    """ prints a square with the character '#'.
    Args:
        size (int): the length of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#' * size)
