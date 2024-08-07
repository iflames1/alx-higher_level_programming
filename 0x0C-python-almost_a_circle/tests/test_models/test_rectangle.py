#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
import os


class TestRectangle(unittest.TestCase):

    """
    def test_valid_arguments(self):

        rect = Rectangle(1, 2)
        self.assertEqual(rect.__dict__,
                         {'_Rectangle__height': 2, '_Rectangle__width': 1,
                          '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 18})

    def test_valid_arguments_with_coordinates(self):

        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.__dict__,
                         {'_Rectangle__height': 2, '_Rectangle__width': 1,
                          '_Rectangle__x': 3, '_Rectangle__y': 4, 'id': 19})
    """

    def test_invalid_type_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_invalid_value_arguments(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_too_many_arguments(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.__dict__,
                         {'_Rectangle__height': 2, '_Rectangle__width': 1,
                          '_Rectangle__x': 3, '_Rectangle__y': 4, 'id': 5})

    def test_area(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_str(self):
        rect = Rectangle(5, 10, 3, 4, 1)
        expected_string = "[Rectangle] (1) 3/4 - 5/10"
        self.assertEqual(str(rect), expected_string)

    def test_invalid_type(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 5)

    def test_width_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 5)

    def test_height_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, -1)

    def test_x_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 5, -1, 0)

    def test_y_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(5, 5, 0, -1)

    def test_rectangle_area(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.area(), 12)

    def test_rectangle_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 4).area()

    def test_rectangle_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 0).area()

    def test_rectangle_str(self):
        rectangle = Rectangle(3, 4, x=1, y=2, id=10)
        self.assertEqual(str(rectangle), "[Rectangle] (10) 1/2 - 3/4")

    """
    def setUp(self):
        self.capturedOutput = StringIO()
        sys.stdout = self.capturedOutput

    def test_rectangle_display(self):
        rectangle = Rectangle(3, 4, x=1, y=2)
        rectangle.display()
        expected_output = "\n\n  ###\n  ###\n  ###\n"
        self.assertEqual(self.capturedOutput.getvalue(), expected_output)
    """

    def test_display_without_x_y(self):
        rect = Rectangle(5, 10)
        rect.display()

    def test_display_without_y(self):
        rect = Rectangle(5, 10, 3)
        rect.display()

    def test_display(self):
        rect = Rectangle(5, 10, 3, 4)
        rect.display()

    def test_to_dictionary(self):
        rect = Rectangle(5, 10, 3, 4, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 3, 'y': 4}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_update_with_args(self):
        rect = Rectangle(5, 10, 3, 4, 1)
        rect.update(89)
        self.assertEqual(rect.__dict__,
                         {'_Rectangle__height': 10, '_Rectangle__width': 5,
                          '_Rectangle__x': 3, '_Rectangle__y': 4, 'id': 89})

    def test_update_with_multiple_args(self):
        rect = Rectangle(5, 10, 3, 4, 1)
        rect.update(89, 1, 2, 3, 4)
        self.assertEqual(rect.__dict__,
                         {'_Rectangle__height': 2, '_Rectangle__width': 1,
                          '_Rectangle__x': 3, '_Rectangle__y': 4, 'id': 89})

    def test_update_with_kwargs(self):
        rect = Rectangle(5, 10, 3, 4, 1)
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(rect.__dict__,
                         {'_Rectangle__height': 2, '_Rectangle__width': 1,
                          '_Rectangle__x': 3, '_Rectangle__y': 4, 'id': 89})

    def test_create_with_id(self):
        rect = Rectangle.create(**{'id': 89})
        self.assertEqual(rect.__dict__,
                         {'_Rectangle__height': 1, '_Rectangle__width': 1,
                          '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 89})

    def test_create_with_width_height(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(rect.__dict__,
                         {'_Rectangle__height': 2, '_Rectangle__width': 1,
                          '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 89})

    def test_create_with_all_arguments(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(rect.__dict__,
                         {'_Rectangle__height': 2, '_Rectangle__width': 1,
                          '_Rectangle__x': 3, '_Rectangle__y': 4, 'id': 89})

    @classmethod
    def setUpClass(cls):
        cls.filename = "Rectangle.json"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_to_file_with_none(self):
        # Test save_to_file() with None argument
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_with_empty_list(self):
        # Test save_to_file() with an empty list
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, "r") as file:
            self.assertEqual(file.read(), "[]")

    """
    def test_save_to_file_with_objects(self):
        # Test save_to_file() with a list of objects
        rectangles = [Rectangle(1, 2), Rectangle(3, 4)]
        Rectangle.save_to_file(rectangles)
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, "r") as file:
            content = file.read()
            print("File Content:", content)
            self.assertNotEqual(content, "[]")
            self.assertTrue('"id": 1' in content)
            self.assertTrue('"id": 2' in content)
            self.assertTrue('"id": 3' in content)
            self.assertTrue('"id": 4' in content)
    """

    def test_load_from_file_file_not_found(self):
        # Test load_from_file() when the file doesn't exist
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_file_exists(self):
        # Test load_from_file() when the file exists
        rectangles = [Rectangle(1, 2), Rectangle(3, 4)]
        Rectangle.save_to_file(rectangles)
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertIsInstance(loaded_rectangles[0], Rectangle)
        self.assertIsInstance(loaded_rectangles[1], Rectangle)
