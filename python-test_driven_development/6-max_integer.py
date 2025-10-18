#!/usr/bin/python3
"""Module to find the max integer in a list
"""

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers.
       If the list is empty, the function returns None.

    Args:
        list (list): A list of integers.

    Returns:
        int: The maximum integer in the list, or None if the list is empty.

    Raises:
        TypeError: If any element in the list is not an integer.
    """
    if len(list) == 0:
        return None
    
    # Check if all elements in the list are integers
    for elem in list:
        if not isinstance(elem, int):
            raise TypeError("All elements in the list must be integers")
    
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
