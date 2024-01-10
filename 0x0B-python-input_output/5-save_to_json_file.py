#!/usr/bin/python3
"""Defines a function save_to_json_file."""


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be saved to the file.
        filename (str): The name of the text file.

    Note:
        You must use the with statement.
        You don’t need to manage exceptions if the object can’t be serialized.
        You don’t need to manage file permission exceptions.
    """
    import json
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
