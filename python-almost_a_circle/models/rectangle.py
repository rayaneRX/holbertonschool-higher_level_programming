#!/usr/bin/python3
""" class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Private instance attributes,each with its own public getter and setter
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def integer_validator(self, name, value):
        """checks the value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def xy_validator(self, name, value):
        """checks the value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        self.integer_validator("height", value)
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.xy_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.xy_validator("y", value)
        self.__y = value


    def area(self):
        """return the area"""
        return self.__width * self.__height

    def display(self):
        """display"""

        for m in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """class Rectangle by overriding the __str__ method"""
        id = self.id
        x = self.x
        y = self.y
        w = self.__width
        h = self.__height
        return f"[Rectangle] ({id}) {x}/{y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute"""
        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.width = args[1]
            if len(args) == 3:
                self.height = args[2]
            if len(args) == 4:
                self.x = args[3]
            if len(args) == 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
