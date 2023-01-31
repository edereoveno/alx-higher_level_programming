#!/usr/bin/python3
"""
    A Rectangle class
"""


class Rectangle():
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """intializes a Rectangle instance
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the value of private instance of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of private instance of width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """retrieves the value of private instance of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of private instance of height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
