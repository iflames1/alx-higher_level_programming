#!/usr/bin/python3
""" module for text_indentation() method """


def text_indentation(text):
    """
    Indents text by adding a new line after periods, question marks, and colons

    Args:
        text (str): The text to indent.

    Raises:
        TypeError: If the input `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    param = ['.', '?', ':']
    index = 0
    while index < len(text):
        if not text[index] in param:
            print(text[index], end='')

        else:
            print(f"{text[index]}\n")
            if not text[index + 1] in param:
                index += 1
        index += 1
