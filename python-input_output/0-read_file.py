#!/usr/bin/python3
"""commands to read a file and print"""


def read_file(filename=""):
    """Reads the file and prints its contants"""
    with open(filename, encoding="utf-8") as f:
               print(f.read(), end="")
