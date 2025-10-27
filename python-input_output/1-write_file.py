#!/usr/bin/python3
"""writes a string in a text file"""


def write_file(filename="", text=""):
    """writes a file and return the number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
