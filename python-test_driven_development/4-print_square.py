#!/usr/bin/python3
"""function that prints a square with the character #."""


def print_square(size):
    """function that prints a square with the character #."""

    if type(size) is not int and type(size) != float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
