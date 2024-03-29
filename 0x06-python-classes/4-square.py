#!/usr/bin/python3
"""
    A module for a square class
"""


class Square():
    """A square class"""
    def __init__(self, size=0):
        """initializes a new square

        Args:
            size(int) size of new square
        """

        self.__size = size

    @property
    def size(self):
        """retrieves tne size"""

        return self.__size

    @size.setter
    def size(self, value):
        """sets the size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area of square"""

        return (self.__size) ** 2
