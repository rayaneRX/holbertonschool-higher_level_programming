#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:"""
    with open(filename, "a") as file:
        file.write(text)
    return len(text)
