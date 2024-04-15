#!/usr/bin/python3
"""Defines a class BaseGeometry based on 6-base_geometry.py"""


class BaseGeometry:
    """Empty BaseGeometry class"""

    def area(self):
        """ Raise an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        # if type(value) is not int:
        #    raise TypeError("{} must be an integer".format(name))

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
