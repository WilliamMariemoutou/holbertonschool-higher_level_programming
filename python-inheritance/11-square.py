#!/usr/bin/python3
"""import the rectangle class"""


Rectangle = __import__("9-rectangle").Rectangle
"""the class square"""


class Square(Rectangle):
    """the class inherits from rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        """validates size"""

        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """returns the string representation of the square"""
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size
