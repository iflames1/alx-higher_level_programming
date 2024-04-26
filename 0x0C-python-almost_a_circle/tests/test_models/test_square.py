#!/usr/bin/python3

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_valid_arguments(self):
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        s2 = Square(1, 2)
        self.assertEqual(s2.x, 2)
        s3 = Square(1, 2, 3)
        self.assertEqual(s3.y, 3)
        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s4.id, 4)

    def test_invalid_type_arguments(self):
        with self.assertRaises(TypeError):
            Square("1", 2)
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_invalid_value_arguments(self):
        with self.assertRaises(ValueError):
            Square(-1, 2)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(0, 2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_area(self):
        sqr = Square(3)
        self.assertEqual(sqr.area(), 9)

    def test_str(self):
        sqr = Square(5, 10, 3, 4)
        expected_string = "[Square] (4) 10/3 - 5"
        self.assertEqual(str(sqr), expected_string)
