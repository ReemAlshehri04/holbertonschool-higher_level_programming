#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
It includes rigorous type checking for both the matrix and the divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): Matrix containing integers or floats.
        div (int/float): The number to divide by.

    Raises:
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
        TypeError: If matrix is invalid or contains non-numbers.
        TypeError: If rows of the matrix are not the same size.

    Returns:
        list: A new matrix with elements rounded to 2 decimal places.
    """
    # 1. Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 2. Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 3. Check if matrix is a list of lists and not empty
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    row_size = None

    for row in matrix:
        # Check if row is a list
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)

        # Check if all rows are the same size
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        # Check if every element in the row is an int or float
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    # 4. Perform division and rounding using nested list comprehension
    # This creates a new matrix and does not modify the original
    return [[round(item / div, 2) for item in row] for row in matrix]
