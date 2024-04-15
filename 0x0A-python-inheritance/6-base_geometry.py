#!/usr/bin/python3
"""Defines a class BaseGeometry based on 5-base_geometry.py"""


class BaseGeometry:
    """BaseGeometry with unimplemented public instance area"""

    def area(self):
        raise Exception("area() is not implemented")
