#!/usr/bin/python3

import unittest
from models.square import Square
import io


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        # Test if the constructor initializes the Square correctly
        s = Square(5, 10, 15, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 15)
        self.assertEqual(s.id, 1)

    def test_area(self):
        # Test if the area method returns the correct area
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_display(self):
        # Test if the display method prints the square correctly
        s = Square(3, 2, 1)
        expected_output = ("\n" + " " * 2 + "###\n" + " " * 2 + "###\n" +
                           " " * 2 + "###\n")
        with (unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
              as mock_stdout):
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        # Test if the update method updates attributes correctly
        s = Square(2, 3, 4, 5)
        s.update(1, 6, 7, 8)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 8)

    def test_to_dictionary(self):
        # Test if the to_dictionary method returns the correct dictionary
        s = Square(3, 4, 5, 6)
        expected_dict = {"id": 6, "size": 3, "x": 4, "y": 5}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
