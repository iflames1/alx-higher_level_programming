#!/usr/bin/python3
"""Defines a class BaseGeometry based on 6-base_geometry.py"""


class BaseGeometry:
    """empty BaseGeometry class"""

    def area(self):
        """ raise exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        Args:
            name (string): name
            value (int): value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
