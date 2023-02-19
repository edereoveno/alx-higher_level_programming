#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
    Square Object Module
"""


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialization of square class"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area of square"""
        return self.__size ** 2

    def __str__(self):
        """
            string descriptor for rectangle
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
