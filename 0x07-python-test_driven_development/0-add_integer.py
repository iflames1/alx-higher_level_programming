#!/usr/bin/python3
""" Function """


def add_integer(a, b=98):
    """_summary_

    Args:
        a (_type_): _description_
        b (int, optional): _description_. Defaults to 98.

    Raises:
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
