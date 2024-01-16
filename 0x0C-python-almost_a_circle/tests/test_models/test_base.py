#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    def setUp(self):
        # Clean up any existing files
        for filename in ["Rectangle.json", "Square.json", "Rectangle.csv",
                         "Square.csv"]:
            try:
                os.remove(filename)
            except FileNotFoundError:
                pass

    def tearDown(self):
        # Clean up any created files after each test
        for filename in ["Rectangle.json", "Square.json", "Rectangle.csv",
                         "Square.csv"]:
            try:
                os.remove(filename)
            except FileNotFoundError:
                pass

    def test_to_json_string(self):
        # Test to_json_string with empty list
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

        # Test to_json_string with a list of dictionaries
        rect = Rectangle(1, 2, 3, 4)
        result = Base.to_json_string([rect.to_dictionary()])
        expected = '[{"id": 1, "width": 1, "height": 2, "x": 3, "y": 4}]'
        self.assertEqual(result, expected)

    def test_save_to_file(self):
        # Test save_to_file with empty list
        Base.save_to_file([])
        self.assertFalse(os.path.exists("Rectangle.json"))

        # Test save_to_file with a list of objects
        rect = Rectangle(1, 2, 3, 4)
        Base.save_to_file([rect])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_from_json_string(self):
        # Test from_json_string with empty string
        result = Base.from_json_string("")
        self.assertEqual(result, [])

        # Test from_json_string with a JSON string
        json_string = '[{"id": 1, "width": 1, "height": 2, "x": 3, "y": 4}]'
        result = Base.from_json_string(json_string)
        expected = [{"id": 1, "width": 1, "height": 2, "x": 3, "y": 4}]
        self.assertEqual(result, expected)

    def test_create(self):
        # Test create method
        rect_dict = {"id": 1, "width": 1, "height": 2, "x": 3, "y": 4}
        result = Rectangle.create(**rect_dict)
        self.assertIsInstance(result, Rectangle)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.width, 1)
        self.assertEqual(result.height, 2)
        self.assertEqual(result.x, 3)
        self.assertEqual(result.y, 4)

    def test_load_from_file(self):
        # Test load_from_file with non-existing file
        result = Base.load_from_file()
        self.assertEqual(result, [])

        # Test load_from_file with an existing file
        rect = Rectangle(1, 2, 3, 4)
        Base.save_to_file([rect])
        result = Base.load_from_file()
        self.assertIsInstance(result[0], Rectangle)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].width, 1)
        self.assertEqual(result[0].height, 2)
        self.assertEqual(result[0].x, 3)
        self.assertEqual(result[0].y, 4)

    def test_save_to_file_csv(self):
        # Test save_to_file_csv with empty list
        Base.save_to_file_csv([])
        self.assertFalse(os.path.exists("Rectangle.csv"))

        # Test save_to_file_csv with a list of objects
        rect = Rectangle(1, 2, 3, 4)
        Base.save_to_file_csv([rect])
        self.assertTrue(os.path.exists("Rectangle.csv"))

    def test_load_from_file_csv(self):
        # Test load_from_file_csv with non-existing file
        result = Base.load_from_file_csv()
        self.assertEqual(result, [])

        # Test load_from_file_csv with an existing file
        rect = Rectangle(1, 2, 3, 4)
        Base.save_to_file_csv([rect])
        result = Base.load_from_file_csv()
        self.assertIsInstance(result[0], Rectangle)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].width, 1)
        self.assertEqual(result[0].height, 2)
        self.assertEqual(result[0].x, 3)
        self.assertEqual(result[0].y, 4)

    def test_draw(self):
        # Test draw method
        rect = Rectangle(100, 40)
        square = Square(35)
        Base.draw([rect], [square])


if __name__ == "__main__":
    unittest.main()
