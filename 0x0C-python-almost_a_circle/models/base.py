#!/usr/bin/python3
import json
import csv


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                list_dicts = [objs.to_dictionary() for objs in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @classmethod
    def save_to_file_csv(cls, list_objs):
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
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                list_dicts = cls.from_json_string(file.read())
                return [cls.create(**dict) for dict in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
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
