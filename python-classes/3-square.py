#!/usr/bin/python3
"""This module defines a Square class that allows computing the area of a square
while ensuring proper size validation.
"""


class Square:
    """This class represents a square defined by a private size attribute."""

    def __init__(self, size=0):
        """Initialize a Square instance with a given size.

        The size of the square must be a non-negative integer.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Compute and return the area of the square.

        The area is calculated by multiplying the size of the square by itself.
        """
        return self.__size * self.__size
