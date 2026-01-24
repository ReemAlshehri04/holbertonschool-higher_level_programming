#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy
    
    Args:
        m_a: first matrix (list of lists of integers/floats)
        m_b: second matrix (list of lists of integers/floats)
    
    Returns:
        product of m_a and m_b
    
    Raises:
        ValueError: if matrices can't be multiplied
    """
    # Let NumPy handle most validation
    try:
        # Convert to numpy arrays - this will catch type errors
        np_a = np.array(m_a, dtype=np.float64)
        np_b = np.array(m_b, dtype=np.float64)
        
        # Perform matrix multiplication
        result = np.matmul(np_a, np_b)
        
        # Convert back to list of lists for consistency
        return result.tolist()
        
    except ValueError as e:
        # Handle shape mismatch errors
        error_msg = str(e)
        if "shape" in error_msg.lower():
            raise ValueError("m_a and m_b can't be multiplied")
        raise
    
    except TypeError as e:
        # Handle type errors (non-numeric data)
        raise TypeError("invalid data type for matrix multiplication")
