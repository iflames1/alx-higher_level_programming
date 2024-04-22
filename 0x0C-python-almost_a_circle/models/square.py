#!/usr/bin/python3
from models.rectangle import Rectangle

"""
Represents a square, which is a specialized form of a rectangle.

The `Square` class inherits from the `Rectangle` class and provides a more
specialized interface for working with square-shaped objects. It adds a `size`
property that allows you to set and get the size of the square, and it
overrides the `__str__` method to provide a more informative string
representation of the square.

The `update` method allows you to update the attributes of the square, either
by passing positional arguments or keyword arguments. The `to_dictionary`
method returns a dictionary representation of the square, which can be useful
for serializing the object.
"""


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the top-left corner of the
            square. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner of the
            square. Defaults to 0.
            id (int, optional): The ID of the square. Defaults to None.
        """
        self.integer_validator("size", size)
        super().__init__(size, size, x, y, id)
        self.__size = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """
        Returns a string representation of the Square object.

        :return: A string in the format "[Square] (id) x/y - size", where id is
        the ID of the square, x and y are the coordinates of the top-left
        corner of the square, and size is the dimension of the square.
        :rtype: str
        """
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__size}"

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size value to set.

        Raises:
            TypeError: If the provided value is not an integer.

        Returns:
            None
        """
        self.integer_validator("width", value)
        self.__size = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square instance based on the arguments
        provided.

        Parameters:
            *args: Variable length argument list. If provided, the arguments
            are interpreted in the order (id, size, x, y).
            **kwargs: Arbitrary keyword arguments. If provided, the following
            keys are processed: 'id', 'size', 'x', and 'y'.

        Returns:
            None
        """
        if args is not None and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.integer_validator("size", args[1])
                self.__size = args[1]
            if len(args) > 2:
                self.integer_validator('x', args[2])
                self.__x = args[2]
            if len(args) > 3:
                self.integer_validator('y', args[3])
                self.__y = args[3]

        elif kwargs is not None:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                elif key == "size":
                    self.integer_validator("size", val)
                    self.__size = val
                elif key == 'x':
                    self.integer_validator("x", val)
                    self.__x = val
                elif key == 'y':
                    self.integer_validator("y", val)
                    self.__y = val

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square object.

        :return: A dictionary containing the 'id', 'size', 'x', and 'y'
        attributes of the Square object.
        :rtype: dict
        """
        return {
            "id": self.id,
            "size": self.__size,
            'x': self.__x,
            'y': self.__y
            }