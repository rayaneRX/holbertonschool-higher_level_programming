#!/usr/bin/python3
""" Write a class Square that defines a square"""


class Square:
    """Private instance attribute: size,Instantiation with optional size
    Public instance method: def area(self): that returns the current square area"""

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, size=0):
        self.__size = size
    
    def area(self):
        return self.__size ** 2
