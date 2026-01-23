#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    matrix must be a list of lists of integers or floats
    div must be a number (int or float)
    """

    # Check matrix type
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check each row is list
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check rectangular matrix
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check each value
    for row in matrix:
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if value != value or value in (float("inf"), float("-inf")):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div != div:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # If div is inf, return zeros
    if div in (float("inf"), float("-inf")):
        return [[0.0 for _ in row] for row in matrix]

    # Perform division
    return [[round(value / div, 2) for value in row] for row in matrix]
