#!/usr/bin/python3

"""This module defines the Base class for object management and serialization.

The Base class provides a foundation for managing objects, converting objects
to and from JSON and CSV formats, and drawing shapes using the Turtle graphics
module.

Attributes:
    __nb_objects (int): A class attribute to keep track of the number of
    objects created.

Methods:
    __init__(self, id=None): Initializes a new instance of the Base class with
    a unique ID.

    to_json_string(list_dictionaries): Converts a list of dictionaries to a
    JSON string.

    save_to_file(cls, list_objs): Saves a list of objects to a JSON file.

    from_json_string(json_string): Converts a JSON string to a list of
    dictionaries.

    create(cls, **dictionary): Creates an instance of the class and updates its
    attributes.

    load_from_file(cls): Loads a list of objects from a JSON file.

    save_to_file_csv(cls, list_objs): Saves a list of objects to a CSV file.

    load_from_file_csv(cls): Loads a list of objects from a CSV file.

    draw(list_rectangles, list_squares): Opens a window and draws rectangles
    and squares using Turtle.

Note:
    The drawing functionality requires the `turtle` module and may need
    additional setup for proper execution.

Usage:
    Example usage of saving and loading from JSON:
        >>> r = Rectangle(10, 20, 30, 40)
        >>> Base.save_to_file([r])
        >>> loaded_objects = Base.load_from_file()
"""
import json
import csv
import turtle


class Base:
    """ class Base """
    
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new instance of the Base class with a unique ID.

        Args:
            id (int): The ID for the instance. If None, a unique ID is
            assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries representing
            objects.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects to be saved.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_data = cls.to_json_string([obj.to_dictionary()
                                        for obj in list_objs])

        with open(filename, 'w') as file:
            file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string representing a list of
            dictionaries.

        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of the class and updates its attributes.

        Args:
            **dictionary: Keyword arguments representing attributes of the
            object.

        Returns:
            obj: An instance of the class with updated attributes.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Loads a list of objects from a JSON file.

        Returns:
            list: A list of objects loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                list_dicts = cls.from_json_string(json_data)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of objects to a CSV file.

        Args:
            list_objs (list): A list of objects to be saved.

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x,
                                     obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of objects from a CSV file.

        Returns:
            list: A list of objects loaded from the CSV file.
        """
        filename = cls.__name__ + ".csv"
        list_objs = []

        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    row = [int(value) for value in row]
                    if cls.__name__ == "Rectangle":
                        obj = cls.create(id=row[0], width=row[1],
                                         height=row[2], x=row[3], y=row[4])
                    elif cls.__name__ == "Square":
                        obj = cls.create(id=row[0], size=row[1], x=row[2],
                                         y=row[3])
                    list_objs.append(obj)
        except FileNotFoundError:
            pass

        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws rectangles and squares using Turtle.

        Args:
            list_rectangles (list): A list of Rectangle objects.
            list_squares (list): A list of Square objects.

        Returns:
            None
        """
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.setup(width=800, height=600)

        pen = turtle.Turtle()
        pen.speed(2)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x - rect.width / 2, rect.y - rect.height / 2)
            pen.pendown()
            pen.color("blue")
            pen.forward(rect.width)
            pen.right(90)
            pen.forward(rect.height)
            pen.right(90)
            pen.forward(rect.width)
            pen.right(90)
            pen.forward(rect.height)
            pen.right(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x - square.size / 2, square.y - square.size / 2)
            pen.pendown()
            pen.color("red")
            for _ in range(4):
                pen.forward(square.size)
                pen.right(90)

        turtle.done()
