#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        self.integer_validator("size", size)
        super().__init__(size, size, x, y, id)
        self.__size = size
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__size}"

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.integer_validator("width", value)
        self.__size = value

    def update(self, *args, **kwargs):
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
