#!/usr/bin/python3
"""A module that create a class Rectangle"""


class Rectangle:
    """A class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif not height > 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif not width > 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
