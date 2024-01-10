#!/usr/bin/python3
"""Defines a function class_to_json."""


def class_to_json(obj):
    """Returns the dictionary description with simple data
     structure for JSON serialization of an object.

    Args:
        obj (object): An instance of a Class with serializable attributes
        (list, dictionary, string, integer, and boolean).

    Returns:
        dict: A dictionary description for JSON serialization of the object.

    Note:
        You are not allowed to import any module.
    """
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
        for key, value in result.items():
            if hasattr(value, "__dict__"):
                result[key] = class_to_json(value)
        return result
    return None
