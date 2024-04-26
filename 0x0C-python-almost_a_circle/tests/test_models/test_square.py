#!/usr/bin/python3

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_square_initialization(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_square_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_square_str_representation(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 5")
