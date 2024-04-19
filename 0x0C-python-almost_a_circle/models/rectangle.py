#!/usr/bin/python3
from models.base import Base

"""
Represents a rectangle object with properties for width, height, x-coordinate,
and y-coordinate. Provides methods for calculating the area, displaying the
rectangle, and updating the rectangle's attributes.

The Rectangle class inherits from the Base class, which provides common
functionality for all objects in the system.
"""


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner of the
            rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner of the
            rectangle. Defaults to 0.
            id (int, optional): The ID of the rectangle. Defaults to None.

        Returns:
            None
        """

        super().__init__(id)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.integer_validator("x", x)
        self.integer_validator("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: A string in the format "[Rectangle] (id) x/y - width/height",
            where id is the ID of the rectangle, x and y are the coordinates of
            the top-left corner of the rectangle, and width and height are the
            dimensions of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "\
            f"{self.__width}/{self.__height}"

    @property
    def width(self):
        """
        Returns the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle.

        Args:
            value (int): The new width value to set.

        Returns:
            None
        """
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value to set.

        Raises:
            TypeError: If the provided value is not an integer.

        Returns:
            None
        """
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """
        Get the x-coordinate of the top-left corner of the rectangle.

        Returns:
            int: The x-coordinate of the top-left corner of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the top-left corner of the rectangle.

        Args:
            value (int): The new x-coordinate value to set.

        Raises:
            TypeError: If the provided value is not an integer.

        Returns:
            None
        """
        self.integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """
        Returns the y-coordinate of the top-left corner of the rectangle.

        Returns:
            int: The y-coordinate of the top-left corner of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the top-left corner of the rectangle.

        Args:
            value (int): The new y-coordinate value to set.

        Raises:
            TypeError: If the provided value is not an integer.

        Returns:
            None
        """
        self.integer_validator('y', value)
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle, which is the product of the width
            and height.
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the rectangle on the console.

        This method prints the rectangle on the console by generating the
        appropriate number of new lines
        based on the `y` attribute and then printing the rectangle shape using
        the `x` attribute to determine
        the starting position of each line and the `width` attribute to
        determine the length of each line.

        Parameters:
            None

        Returns:
            None
        """
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(f"{' ' * self.__x}{'#' * self.__width}")

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle instance based on the arguments
        provided.

        Parameters:
            *args: Variable length argument list. If provided, the arguments
            are interpreted in the order (id, width, height, x, y).
            **kwargs: Arbitrary keyword arguments. If provided, the following
            keys are processed: 'id', 'width', 'height', 'x', and 'y'.

        Returns:
            None
        """
        if args is not None and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.integer_validator("width", args[1])
                self.__width = args[1]
            if len(args) > 2:
                self.integer_validator("height", args[2])
                self.__height = args[2]
            if len(args) > 3:
                self.integer_validator('x', args[3])
                self.__x = args[3]
            if len(args) > 4:
                self.integer_validator('y', args[4])
                self.__y = args[4]

        elif kwargs is not None:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                elif key == "width":
                    self.integer_validator("width", val)
                    self.__width = val
                elif key == "height":
                    self.integer_validator("height", val)
                    self.__height = val
                elif key == 'x':
                    self.integer_validator("x", val)
                    self.__x = val
                elif key == 'y':
                    self.integer_validator("y", val)
                    self.__y = val

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Rectangle object.

        :return: A dictionary containing the 'id', 'width', 'height', 'x', and
        'y' attributes of the Rectangle object.
        :rtype: dict
        """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            'x': self.__x,
            'y': self.__y
            }
