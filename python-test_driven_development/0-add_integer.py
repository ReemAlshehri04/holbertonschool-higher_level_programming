#!/usr/bin/python3
"""
Module that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to int).

    Args:
        a (int or float)
        b (int or float)

    Raises:
        TypeError: if a or b is not an integer or float
    Returns:
        int: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Reject NaN and Infinity for a
    if a != a or a in (float('inf'), float('-inf')):
        raise TypeError("a must be an integer")

    # Reject NaN and Infinity for b
    if b != b or b in (float('inf'), float('-inf')):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
