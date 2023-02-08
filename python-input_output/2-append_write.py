#!/usr/bin/python3
"""unction that appends a string at the end of a text file (UTF8)"""


def write_file(filename="", text=""):
    """returns the number of characters added"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
    return len(text)
