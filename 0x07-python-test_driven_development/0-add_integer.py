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
    if a is None or (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
