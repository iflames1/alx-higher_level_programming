#!/usr/bin/python3
""" Test Base class """

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

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
        obj1 = Base()
        self.assertEqual(obj1.id, 6)


class TestBaseToJsonString(unittest.TestCase):

    def test_none_input(self):

        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_empty_list(self):

        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_single_dict_list(self):

        input_data = [{'id': 12}]
        expected_result = '[{"id": 12}]'
        result = Base.to_json_string(input_data)
        self.assertEqual(result, expected_result)

    def test_multiple_dict_list(self):

        input_data = [{'id': 12}, {'id': 15}]
        expected_result = '[{"id": 12}, {"id": 15}]'
        result = Base.to_json_string(input_data)
        self.assertEqual(result, expected_result)


class TestBaseFromJsonString(unittest.TestCase):
    def test_none_input(self):

        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_empty_string_input(self):

        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_single_dict_string(self):

        input_string = '[{ "id": 89 }]'
        expected_result = [{'id': 89}]
        result = Base.from_json_string(input_string)
        self.assertEqual(result, expected_result)

    def test_multiple_dict_string(self):

        input_string = '[{ "id": 89 }, { "id": 90 }]'
        expected_result = [{'id': 89}, {'id': 90}]
        result = Base.from_json_string(input_string)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
