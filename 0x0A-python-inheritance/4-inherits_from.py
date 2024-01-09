#!/usr/bin/python3
"""Module that defines a function inherits_from."""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherited
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class.

    Returns:
        True if the object is an instance of a class that inherited
        from the specified class;
        otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
