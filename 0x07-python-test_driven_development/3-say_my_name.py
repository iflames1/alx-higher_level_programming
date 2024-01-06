#!/usr/bin/python3
""" module for say_my_name() method """


def say_my_name(first_name, last_name=""):
    """ prints My name is <first name> <last name>
    Args:
        first_name: First Name
        last_name: Last Name
    Raises:
        TypeError: if first_name or last_name is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
