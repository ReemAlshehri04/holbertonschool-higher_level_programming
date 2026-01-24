#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
It validates the matrix structure and the divisor before performing operations.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor (div).

    Args:
        matrix (list of lists): A list of lists of integers or floats.
        div (int/float): The number to divide by.

    Raises:
        TypeError: If the matrix is not a list of lists of numbers.
        TypeError: If rows of the matrix are of different sizes.
        TypeError: If div is not a number (int or float).
        ZeroDivisionError: If div is 0.

    Returns:
        list: A new matrix with values rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if matrix is a list and not empty
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    row_length = None

    for row in matrix:
        # Check if each row is a list
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)

        # Ensure all rows are the same length
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        # Validate that every element in the row is an int or float
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    # Return new matrix using list comprehension
    return [[round(element / div, 2) for element in row] for row in matrix]
