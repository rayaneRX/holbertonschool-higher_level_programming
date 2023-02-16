#!/usr/bin/python3
"""Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        self.id = id
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    def __str__(self):
        id = self.id
        x = self.x
        y = self.y
        s = self.size
        return f"[Square] ({id}) {x}/{y} - {s}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute"""
        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.size = args[1]
            if len(args) == 3:
                self.x = args[2]
            if len(args) == 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """eturns the dictionary representation of a Rectangle"""

        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
