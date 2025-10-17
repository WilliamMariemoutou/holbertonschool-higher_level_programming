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

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height
    """returns the area of the rectangle"""

    def perimeter(self):
        """calculates he perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    """returns the width of the rectangle"""

    def __str__(self):
        """string to represent the rectaangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        """if width or height is 0, print an empty string"""
        return "\n".join(["#" * self.__width] * self.__height)
    """prints the rectangle"""
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    """returns the representation of the rectangle"""

    def __del__(self):
        print("Bye rectangle...")
        """prints a message when the rectangle is deleted"""
