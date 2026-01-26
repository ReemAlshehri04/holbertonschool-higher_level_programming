#!/usr/bin/python3
"""This module defines a Square class with a private size attribute."""


class Square:
    """This class defines a square by its size."""

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size: The size of the square (no type or value validation).
        """
        self.__size = size
