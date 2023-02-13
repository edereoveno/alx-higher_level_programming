#!/usr/bin/python3

"""
A module of a square class
"""


class Square():
    """A square class"""

    def __init__(self, size=0):
        """instantiation"""

        self.__size = size

    @property
    def size(self):
        """retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of square"""

        self.__size = value

    def area(self):
        """gets area of square"""

        return self.__size ** 2

    def my_print(self):
        """print of square with character #"""
        size = self.__size
        if size == 0:
            print()
        for i in range(size):
            for j in range(size):
                print('#', end="")
            print()
