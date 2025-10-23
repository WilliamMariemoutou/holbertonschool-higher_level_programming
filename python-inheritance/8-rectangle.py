#!/usr/bin/python3
"""the base geometry class """
class BaseGeometry:
    """the class with are and integer_validation"""

    def area(self):
        raise Exception("area() is not implemented")
    """raise exception if area is not implemented"""

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        """return typeerror is value is not an integer"""
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        """return value error is value is not greater than 0"""


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
