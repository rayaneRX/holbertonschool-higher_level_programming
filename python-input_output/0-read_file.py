#!/usr/bin/python3
# 0-read_file.py
# Brennan D Baraban <375@holbertonschool.com>
"""function that reads a text file (UTF8)"""


def read_file(filename=""):
    """prints it to stdout:"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
