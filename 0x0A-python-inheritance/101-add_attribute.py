#!/usr/bin/python3
"""Defines a function add_attribute."""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if it's possible.

    Args:
        obj: The object to add the attribute to.
        attribute (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if isinstance(obj, (dict, list, set, tuple, str, int, float)):
        raise TypeError("can't add new attribute")

    settattr(obj, attribute, value)
