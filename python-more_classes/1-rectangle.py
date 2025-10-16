#!/usr/bin/python3
"""creates a class rectangle"""


class Rectangle:
    """the class rectangle with width and height"""
    def __init__(self, width=0, height=0):
        """creates a new rectangle"""
        self.width = width
        """width of the rectangle"""
        self.height = height
        """height of the rectangle"""

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width
        """returns the width og the rectangle"""

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        """TypeError: if width is not an integer"""
        if value < 0:
            raise ValueError("width must be >= 0")
        """ValueError: if width is less than 0"""
        self.__width = value
        """return the value"""

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height
    """returns the height"""

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        """TypeError: if the height is not an integer"""
        if value < 0:
            raise ValueError("height must be >= 0")
        """ValueError: if the height is less than 0"""
        self.__height = value
        """return the value"""
