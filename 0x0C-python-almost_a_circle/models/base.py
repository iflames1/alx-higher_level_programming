#!/usr/bin/python3
"""
Initializes a new instance of the Base class.

Args:
    id (int, optional): The ID of the instance. If not provided, a new ID will
    be generated.

Returns:
    None
"""

import json
import csv


class Base:
    """ Base of all classes in this project """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the class.

        Args:
            id (int, optional): The ID of the instance. If not provided,
            a new ID will be generated.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
        """
        Validates if the given value is an integer and meets the specified
        conditions.

        Args:
            name (str): The name of the variable being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0 and the name is
            "width", "height", or "size".
                       If the value is less than 0 and the name is 'x' or 'y'.

        Returns:
            None
        """
        if isinstance(value, int) is False:
            raise TypeError(f"{name} must be an integer")

        if name == "width" and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if name == "height" and value <= 0:
            raise ValueError("{} must be > 0".format(name))

        if name == "size" and value <= 0:
            raise ValueError("{} must be > 0".format(name))

        if name == 'x' and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        if name == 'y' and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (List[Dict]): A list of dictionaries to be
            converted to JSON.

        Returns:
            str: A JSON string representation of the input list of dictionaries
            If the input is None or empty, returns "[]".
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation of a list of dictionaries to a
        list of dictionaries.

        Args:
            json_string (str): A JSON string representation of a list of
            dictionaries.

        Returns:
            list: A list of dictionaries. If the input is None or empty,
            returns an empty list.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            cls: The class.
            list_objs: A list of objects to be saved.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                list_dicts = [objs.to_dictionary() for objs in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of objects to a CSV file.

        Args:
            cls: The class.
            list_objs: A list of objects to be saved.

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new instance of the class based on the provided dictionary.

        Parameters:
            **dictionary (dict): A dictionary containing the attributes and
            their values to be set on the new instance.

        Returns:
            object: A new instance of the class with the attributes set
            according to the provided dictionary.

        Raises:
            None

        This class method creates a new instance of the class based on the
        provided dictionary. It first checks if the class name is "Rectangle"
        or "Square" and creates a new instance with the appropriate arguments.
        Then, it calls the `update` method of the new instance to set the
        attributes according to the provided dictionary. Finally, it returns
        the new instance.
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Load objects from a JSON file.

        This class method loads objects from a JSON file and returns a list of
        created objects.

        Parameters:
            cls (class): The class object.

        Returns:
            list: A list of created objects.

        Raises:
            FileNotFoundError: If the JSON file does not exist.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                list_dicts = cls.from_json_string(file.read())
                return [cls.create(**dict) for dict in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """
        Load objects from a CSV file and create instances of the class.

        This class method loads objects from a CSV file and creates instances
        of the class using the data in the file. The file name is constructed
        by appending ".csv" to the class name. The file is expected to have a
        header row with the field names. The field names are used to map the
        data in the file to the attributes of the class instances.

        Returns:
            A list of instances of the class created from the data in the CSV
            file. If the file is not found, an empty list is returned.

        Raises:
            FileNotFoundError: If the CSV file is not found.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(file, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
