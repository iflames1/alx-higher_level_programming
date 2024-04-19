#!/usr/bin/python3

from models.rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):

    def test_rectangle_area(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)
