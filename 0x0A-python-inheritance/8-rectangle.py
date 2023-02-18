#!/usr/bin/python3
"""Module defines class Rectangle"""


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
