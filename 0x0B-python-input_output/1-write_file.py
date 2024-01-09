#!/usr/bin/python3
"""Defines a function write_file."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return the number of
    characters written.

    Args:
        filename (str): The name of the text file.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding="utf=8") as file:
        return file.write(text)
