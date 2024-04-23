#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):

    def test_rectangle_area(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_invalid_type(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 5)

    def test_width_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 5)

    def test_height_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, -1)

    def test_x_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 5, -1, 0)

    def test_y_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(5, 5, 0, -1)
