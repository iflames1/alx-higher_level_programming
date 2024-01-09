#!/usr/bin/python3
"""Defines a function to_json_string."""


def to_json_string(my_obj):
    """Return the JSON representation of an object (string).

    Args:
        my_obj: The object to be converted to a JSON string.

    Returns:
        str: The JSON representation of the object.
    """
    import json
    return json.dumps(my_obj)
