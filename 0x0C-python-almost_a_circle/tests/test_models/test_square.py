#!/usr/bin/python3

from models.square import Square
import unittest

class TestSquare(unittest.TestCase):

    def test_square_area(self):
        sq = Square(5)
        self.assertEqual(sq.area(), 25)
