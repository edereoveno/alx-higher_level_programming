#!/usr/bin/python3
"""Module of Rectangle class that inherits from Base"""
from base import Base


class Rectangle(Base):
    """A Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """gets rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets rectangle width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets rectangle height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x value"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """gets y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y value"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints Rectangle represented by # in stdout"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("{}".format("#"), end="")
            print()

    def __str__(self):
        """return new str"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))
