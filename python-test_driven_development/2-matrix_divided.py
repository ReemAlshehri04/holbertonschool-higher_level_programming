#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
The module ensures high reliability through strict type and value checking.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor (div).

    Args:
        matrix (list of lists): A matrix containing integers or floats.
        div (int/float): The number used for division.

    Raises:
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is equal to zero.
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.

    Returns:
        list: A new matrix with result values rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Check if div is a number (handles the 'div=string' test case)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 2. Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 3. Validate matrix type and structure
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    row_size = None

    for row in matrix:
        # Check if row is a list
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)

        # Validate consistent row size
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        # Validate elements inside the row
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    # 4. Return new matrix with rounded division
    return [[round(item / div, 2) for item in row] for row in matrix]
