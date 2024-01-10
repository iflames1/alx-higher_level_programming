#!/usr/bin/python3
""" Module for add_integer method """


def add_integer(a, b=98):
    """ Adds 2 integer.

    Args:
        a: first argument
        b: second argument
    Raises:
        TypeError: if a or b is not an integer or float

    Returns (int): addition of a and b
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
