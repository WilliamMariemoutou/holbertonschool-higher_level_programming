#!/usr/bin/python3
"""This class defines a square"""


class Square:
    """this class defines a square with a specific size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square with a specified size"""
        self.size = size
        """the size of the square"""
        self.position = position
        """the positiion of the square"""

    @property
    def size(self):
        """get the size of the square"""
        return self.__size
        """returns the size of the square"""

    @size.setter
    def size(self, value):
        """set the size of the square, must be positive"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        """TypeError: if size is not an integer"""
        if value < 0:
            raise ValueError("size must be >= 0")
        """ValueError: if size is less than 0"""
        self.__size = value
        """Returns the value"""

    @property
    def position(self):
        """get the position of the square"""
        return self.__position
    """returns the position"""

    @position.setter
    def position(self, value):
        """set the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        """TypeError: if position is not a tuple of 2 integers"""
        if any(type(i) is not int or i < 0 for i in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        """ValueError: if any elements is less than 0"""

        self.__position = value
        """returns the value of the tuple"""

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2
    """returns the area of the square"""

    def my_print(self):
        """prints the square using this character '#'"""
        if self.__size == 0:
            """checks if the size square is 0"""
            print("")
            """prints an empty line"""
            return
        """the square using the # character"""

        for _ in range(self.__position[1]):
            print("")
            """prints the vertical line based on position[1]"""

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
            """prints the hozizontal line based on position[0]"""
