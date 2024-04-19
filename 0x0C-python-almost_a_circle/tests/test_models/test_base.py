#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_id(self):

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        # Test integer_validator method with valid inputs
        base = Base()
        self.assertIsNone(base.integer_validator("test", 5))

        # Test integer_validator method with invalid inputs
        with self.assertRaises(TypeError):
            base.integer_validator("test", "string")
        with self.assertRaises(ValueError):
            base.integer_validator("width", 0)

