#!/usr/bin/python3
"""A module that create a class Rectangle"""


class Rectangle:
    """A class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """A public instance method that returns the area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """A public instance method that returns the perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2
    
    def __str__(self):
        dan = ""
        for i in range(self.__height):
            if self.__height == 0 or self.__width == 0:
                return ""
            else:
                dan += "#" * self.__width + "\n"
        return dan
