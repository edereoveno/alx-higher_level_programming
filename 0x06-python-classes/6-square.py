#!/usr/bin/python3

"""
A module of a square class
"""


class Square():
    """A square class"""

    def __init__(self, size=0, position=(0, 0)):
        """instantiation"""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retrieves position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """print of square with character # at a position"""
        size = self.__size
        position = self.__position
        if size == 0:
            print()
            return
        for l in range(position[1]):
            print()
        for i in range(size):
            for j in range(position[0]):
                print(' ', end="")
            for k in range(size):
                print('#', end="")
            print()
