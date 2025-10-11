#!/usr/bin/python3
"""
This module provides a function `matrix_divided` that divides all elements 
of a matrix by a divisor while handling input validation and exceptions.

Exceptions handled:
- TypeError: For invalid matrix or divisor types.
- ZeroDivisionError: For division by zero.

Functions:
    matrix_divided(matrix, div): Divides all elements of a matrix by div.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Parameters:
        matrix (list of lists): Matrix of integers or floats.
        div (int/float): The divisor (cannot be zero).

    Returns:
        list of lists: Matrix with each element divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of numbers or rows are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """
    
    # Validate the matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Validate the divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Perform division and return the new matrix
    return [[round(element / div, 2) for element in row] for row in matrix]
