#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Class representing an integer with inverted equality operators."""

    def __eq__(self, other):
        """Invert the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the inequality operator."""
        return super().__eq__(other)
