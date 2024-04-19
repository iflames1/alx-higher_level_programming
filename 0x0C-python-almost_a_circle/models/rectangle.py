#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):


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
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
           print(f"{' ' * self.__x}{'#' * self.__width}")

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            super().__init__(args[0])
            if len(args) > 1:
                self.integer_validator("width", args[1])
                self.__width = args[1]
            if len(args) > 2:
                self.integer_validator("height", args[2])
                self.__height = args[2]
            if len(args) > 3:
                self.integer_validator("x", args[3])
                self.__x = args[3]
            if len(args) > 4:
                self.integer_validator("y", args[4])
                self.__y = args[4]
        elif kwargs is not None:
            for key, val in kwargs.items():
                if key == "id":
                    super().__init__(val)
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
