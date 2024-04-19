#!/usr/bin/python3
import json


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

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [objs.to_dictionary() for objs in list_objs]
                file.write(cls.to_json_string(list_dicts))
