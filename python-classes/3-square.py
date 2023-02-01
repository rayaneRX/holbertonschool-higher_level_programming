#!/usr/bin/python3
"""class Square that defines a square """


class Square:
    """cPrivate instance attribute: size Instantiation with optional """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return self.__size ** 2
