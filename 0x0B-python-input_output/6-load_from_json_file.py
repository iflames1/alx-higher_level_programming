#!/usr/bin/python3
"""Defines a function load_from_json_file."""


def load_from_json_file(filename):
    """Create an Object from a “JSON file”.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python data structure represented by the JSON file.

    Note:
        You must use the with statement.
        You don’t need to manage exceptions if the JSON string doesn’t represent an object.
        You don’t need to manage file permissions / exceptions.
    """
    import json
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
