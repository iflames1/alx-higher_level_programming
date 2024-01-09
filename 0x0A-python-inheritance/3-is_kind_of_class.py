#!/usr/bin/python3
"""Module that defines a function is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of, or if it inherited from,
    the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class.

    Returns:
        True if the object is an instance of, or inherited from,
        the specified class;
        otherwise, False.
    """
    return isinstance(obj, a_class)
