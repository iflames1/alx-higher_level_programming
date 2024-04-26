#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


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

    def test_update_method(self):
        r = Rectangle(1, 2, 3, 4)
        r.update(5, 6, 7, 8, 9)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 9)

        r.update(id=10, width=11, height=12, x=13, y=14)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 11)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 13)
        self.assertEqual(r.y, 14)
