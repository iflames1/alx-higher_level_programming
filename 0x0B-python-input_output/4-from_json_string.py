#!/usr/bin/python3
"""Defines a function from_json_string."""


def from_json_string(my_str):
    """Return an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON-formatted string.

    Returns:
        object: The Python data structure represented by the JSON string.

    Note:
        You don’t need to manage exceptions if the JSON string does not
        represent an object.
    """
    import json
    return json.loads(my_str)
