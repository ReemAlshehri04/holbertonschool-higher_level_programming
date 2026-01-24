#!/usr/bin/python3
"""
Module for matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices
    
    Args:
        m_a: first matrix (list of lists of integers/floats)
        m_b: second matrix (list of lists of integers/floats)
    
    Returns:
        product of m_a and m_b
    
    Raises:
        TypeError: if m_a or m_b is not a list of lists of integers/floats
        ValueError: if m_a or m_b is empty or can't be multiplied
    """
    # Validate m_a is a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    
    # Validate m_b is a list
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    # Validate m_a is a list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    
    # Validate m_b is a list of lists
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    # Validate m_a is not empty
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    
    # Validate m_b is not empty
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    
    # Validate all elements in m_a are integers or floats
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    
    # Validate all elements in m_b are integers or floats
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    
    # Validate all rows in m_a have same size
    if len(m_a) > 0:
        row_size_a = len(m_a[0])
        for row in m_a:
            if len(row) != row_size_a:
                raise TypeError("each row of m_a must be of the same size")
    
    # Validate all rows in m_b have same size
    if len(m_b) > 0:
        row_size_b = len(m_b[0])
        for row in m_b:
            if len(row) != row_size_b:
                raise TypeError("each row of m_b must be of the same size")
    
    # Validate matrices can be multiplied
    # Number of columns in m_a must equal number of rows in m_b
    if len(m_a) > 0 and len(m_b) > 0:
        if len(m_a[0]) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")
    
    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            # Calculate dot product of row i of m_a and column j of m_b
            dot_product = 0
            for k in range(len(m_b)):
                dot_product += m_a[i][k] * m_b[k][j]
            result_row.append(dot_product)
        result.append(result_row)
    
    return result
