#!/usr/bin/python3
"""
Module that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to int).
    """

    try:
        a = int(a)
    except (TypeError, ValueError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (TypeError, ValueError):
        raise TypeError("b must be an integer")

    return a + b
