#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """

    if (not isinstance(matrix, list) or
            matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if matrix contains valid numbers (no nan/inf)
    for row in matrix:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if num != num or num == float("inf") or num == float("-inf"):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("matrix must have each row with the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div != div:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # If div is inf, all results should be 0.0
    if div == float("inf") or div == float("-inf"):
        return [[0.0 for _ in row] for row in matrix]

    new_matrix = []
    for row in matrix:
        new_matrix.append([round(num / div, 2) for num in row])

    return new_matrix
