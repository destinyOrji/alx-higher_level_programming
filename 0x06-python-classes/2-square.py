#!/usr/bin/python3

class Square:
    """This class defines a square.

    Attributes:
        __size (int): The side length of the square.
    """

    def __init__(self, size=0):
        """Initialize the Square instance with an optional size.

        Args:
            size (int, optional): The side length of the square. Defaults to 0.
        """
        # Use a private attribute to store the size
        self.__size = size

        # Check if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Check if size is greater than or equal to 0
        if size < 0:
            raise ValueError("size must be >= 0")
