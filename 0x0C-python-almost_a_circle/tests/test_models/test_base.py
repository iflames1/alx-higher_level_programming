#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_id_attribute(self):

        b1 = Base()
        self.assertIsInstance(b1.id, int)
        self.assertTrue(b1.id > 0)

        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_integer_validator(self):
        base = Base()

        # Test integer_validator method with valid inputs
        self.assertIsNone(base.integer_validator("test", 5))

        # Test integer_validator method with valid inputs
        with self.assertRaises(TypeError):
            base.integer_validator("test", "string")
        with self.assertRaises(ValueError):
            base.integer_validator("width", 0)




if __name__ == "__main__":
    unittest.main()