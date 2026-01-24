#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
It performs strict type checking for the matrix and the divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): A list of lists of integers or floats.
        div (int or float): The number to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        A new matrix containing the division results rounded to 2 decimal places.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if matrix is a list and not empty
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)

    row_len = None

    for row in matrix:
        # Check if each row is a list and not empty
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(error_msg)

        # Check if all rows are the same size
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        # Check if elements in row are integers or floats
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)

    # Return a new matrix with divided and rounded elements
    return [[round(item / div, 2) for item in row] for row in matrix]
