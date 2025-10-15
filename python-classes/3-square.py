#!/usr/bin/python3
"""This class defines a square"""


class Square:
    """This class defines a square with a specific size"""

    def __init__(self, size=0):
        """
        Initializes a new instance
        size: the size of the square
        """
        if not isinstance(size, int):
            raise TypeError
        """TypeError: if size is not an integer"""

        if size < 0:
            raise ValueError("size must be >= 0")
        """ValueError: if size is less than 0"""

        self.__size = size
        """the size of the square, must be positive"""

    def area(self):
        """Claculate the area of the square"""

        return self.__size ** 2
    """return the area of the square"""
