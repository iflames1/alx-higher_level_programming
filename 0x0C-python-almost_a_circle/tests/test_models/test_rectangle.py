#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        # Test if the constructor initializes the Rectangle correctly
        r = Rectangle(4, 5, 10, 15, 1)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 15)
        self.assertEqual(r.id, 1)

    def test_area(self):
        # Test if the area method returns the correct area
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_display(self):
        # Test if the display method prints the rectangle correctly
        r = Rectangle(3, 2)
        expected_output = "###\n" + "###\n"
        with (unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
              as mock_stdout):
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        # Test if the update method updates attributes correctly
        r = Rectangle(2, 3, 4, 5, 6)
        r.update(1, 7, 8, 9, 10)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 10)

    def test_to_dictionary(self):
        # Test if the to_dictionary method returns the correct dictionary
        r = Rectangle(3, 4, 5, 6, 7)
        expected_dict = {"id": 7, "width": 3, "height": 4, "x": 5, "y": 6}
        self.assertEqual(r.to_dictionary(), expected_dict)
