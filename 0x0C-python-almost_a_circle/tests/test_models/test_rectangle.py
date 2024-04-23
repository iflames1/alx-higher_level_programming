#!/usr/bin/python3

from io import StringIO
import sys
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

    def test_rectangle_area(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.area(), 12)

    def test_rectangle_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 4).area()

    def test_rectangle_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 0).area()

    def test_rectangle_str(self):
        rectangle = Rectangle(3, 4, x=1, y=2, id=10)
        self.assertEqual(str(rectangle), "[Rectangle] (10) 1/2 - 3/4")

    #def setUp(self):
    #    self.capturedOutput = StringIO()
    #    sys.stdout = self.capturedOutput

    #def test_rectangle_display(self):
    #    rectangle = Rectangle(3, 4, x=1, y=2)
    #    rectangle.display()
    #    expected_output = "\n\n  ###\n  ###\n  ###\n"
    #    self.assertEqual(self.capturedOutput.getvalue(), expected_output)
