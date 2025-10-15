#!/usr/bin/python3
"""This class defines a square"""


class Square:
    """This class defines a square with a specific size"""
    def __init__(self, size=0):
        """
        Initialize a new square instance.
        size: the size of the square
        """
        if not isinstance(size, int):
            raise TypeError
        """TypeError: if size is not an integer
        """

        if size < 0:
            raise ValueError("size must be >= 0")
        """"
        ValueError: if size is less than 0
        """

        self.__size = size
        """the size of the square, must not be negative
        """
