#!/usr/bin/python3
"""the base geometry class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""the class rectangle"""


class Rectangle(BaseGeometry):
    """the class inherits from basegeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        """validates width and height"""

        self.__width = width
        self.__height = height
        """calls child and parent method"""
