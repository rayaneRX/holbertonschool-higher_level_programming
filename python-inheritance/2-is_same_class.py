#!/usr/bin/python3
""" function that returns True if the object is 
exactly an instance of the specified class ; otherwise False."""


def is_same_class(obj, a_class):
    """ function that returns True if the object is 
exactly an instance of the specified class ; otherwise False."""
    tph = isinstance(obj, a_class)
    if tph:
        return True
    else:
        return False
