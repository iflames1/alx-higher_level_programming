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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
