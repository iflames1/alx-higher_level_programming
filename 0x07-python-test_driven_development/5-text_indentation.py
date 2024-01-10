#!/usr/bin/python3
""" module for text_indentation() method """


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    param = ['.', '?', ':']
    index = 0
    while index < len(text):
        char = text[index]
        if char in param:
            print("\n\n", end="")
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1

        elif char != '\n':
            print(char, end="")
        index += 1
