#!/usr/bin/python3
""" Test Base class """

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Test Base class """

    def test_id_not_none(self):

        b1 = Base()
        self.assertIsNotNone(b1.id)

    def test_auto_assign_id(self):

        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_auto_assign_id_increment(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 3)
        self.assertEqual(obj2.id, 4)
        self.assertEqual(obj3.id, 5)

    def test_custom_id(self):
        obj = Base(89)
        self.assertEqual(obj.id, 89)


if __name__ == "__main__":
    unittest.main()