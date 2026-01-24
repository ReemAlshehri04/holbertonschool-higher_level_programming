def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor (div).

    Args:
        matrix: A list of lists of integers or floats.
        div: The number (int or float) to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix with the results rounded to 2 decimal places.
    """
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if matrix is a list
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = None

    for row in matrix:
        # Check if each row is a list
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        # Check if all rows are the same size
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        # Check if all elements in row are integers or floats
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Perform division and rounding
    return [[round(element / div, 2) for element in row] for row in matrix]
