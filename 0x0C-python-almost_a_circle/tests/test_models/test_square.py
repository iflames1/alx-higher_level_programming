#!/usr/bin/python3

#!/usr/bin/python3

from io import StringIO
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
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

    def test_update_with_args(self):
        square = Square()
        square.update(1, 10, 5, 3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 3)

    def test_update_with_kwargs(self):
        square = Square()
        square.update(id=2, size=15, x=8, y=6)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 6)

    def test_update_with_args_and_kwargs(self):
        square = Square()
        square.update(3, size=20, x=12, y=9)
        self.assertEqual(square.id, 3)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 12)
        self.assertEqual(square.y, 9)

