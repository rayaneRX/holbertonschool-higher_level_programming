#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Write a class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Write a class Rectangle that inherits from BaseGeometry"""

        
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height