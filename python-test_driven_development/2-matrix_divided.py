#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
It handles various edge cases including type checking and zero division.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor (div).

    Args:
        matrix (list of lists): Must be integers or floats.
        div (int/float): The number to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list: A new matrix with results rounded to 2 decimal places.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 2. Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 3. Check if matrix is a list
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(error_msg)

    row_length = None

    for row in matrix:
        # Check if row is a list
        if not isinstance(row, list) or not row:
            raise TypeError(error_msg)

        # Check if all elements in row are numbers
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)

        # Check row size consistency
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # 4. Perform division and rounding
    return [[round(num / div, 2) for num in row] for row in matrix]
