#!/usr/bin/python3
""" class Rectangle that inherits from Base"""
Base = __import__('models').Base


class Rectangle(Base):
    """Private instance attributes,
    each with its own public getter and setter:
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
