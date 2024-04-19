#!/usr/bin/python3


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
