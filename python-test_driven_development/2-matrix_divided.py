#!/usr/bin/python3
"""
Module for matrix division
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
        matrix: list of lists of integers/floats
        div: number (integer or float) to divide by

    Returns:
        new matrix with all elements divided by div, rounded to 2 decimal places

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats,
                   or if rows have different sizes,
                   or if div is not a number
        ZeroDivisionError: if div is zero
    """
    # Validate matrix type
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    
    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Validate each row
    row_len = None
    for row in matrix:
        # Check row is a list
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        
        if len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        
        # Check row length consistency
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        
        # Check elements are integers/floats
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create new matrix with divided values
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            # Round to 2 decimal places after division
            result = round(element / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix
