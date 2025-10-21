#!/usr/bin/python3
"""defines a class MyList that inherits from the list class"""


class MyList(list):
    """the subclass of the list, prints in ascending order"""

    def print_sorted(self):
        """prints the elements of the list in ascending order"""

        print(sorted(self))
