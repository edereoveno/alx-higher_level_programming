#!/usr/bin/python3
"""
    Square Object Module
"""
Rectangle = __import__('9-rectangle').Rectangle


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
        return "[Square] {}/{}".format(self.__size, self.__size)
