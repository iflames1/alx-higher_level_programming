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

    def test_to_dictionary(self):
        sqr = Square(5, 10, 4, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 10, 'y': 4}
        self.assertEqual(sqr.to_dictionary(), expected_dict)

    """
    def test_update_with_args(self):
        sqr = Square(5, 3, 4, 1)
        sqr.update(89)
        self.assertEqual(sqr.__dict__,
                         {'_Square__width': 5,
                          '_Square__x': 3, '_Square__y': 4, 'id': 89})

    def test_update_with_multiple_args(self):
        sqr = Square(5, 3, 4, 1)
        sqr.update(89, 1, 3, 4)
        self.assertEqual(sqr.__dict__,
                         {'_Square__size': 1,
                          '_Square__x': 3, '_Square__y': 4, 'id': 89})

    def test_update_with_kwargs(self):
        sqr = Square(5, 10, 3, 1)
        sqr.update(**{'id': 89, 'size': 1, 'x': 3, 'y': 4})
        self.assertEqual(sqr.__dict__,
                         {'_Square__width': 1,
                          '_Square__x': 3, '_Square__y': 4, 'id': 89})
    """
