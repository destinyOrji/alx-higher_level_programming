#!/usr/bin/python3
# 0-square.py by orji destiny
"""creating an emptySquare class"""

class Square:
    """This class represents a square.

    It is initialized with a size attribute that defines the side length of the square.

    Attributes:
        __size (int): The side length of the square.
    """

    def __init__(self, size):
        """Initialize the Square instance with a given size.

        Args:
            size (int): The side length of the square.
        """
        self.__size = size

