#!/usr/bin/python3
"""Write a function that app a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """returns the number of characters written"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
    return len(text)
