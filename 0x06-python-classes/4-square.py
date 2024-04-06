#!/usr/bin/python3
"""A module that defines a class called Square"""
class Square:
    """A class called Square"""
    def __init__(self, size=0):
        """The constructor of the instances of Square"""
        self.__size = size

    @property
    def size(self):
        """A method called getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """The setter of the object"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """A method to find the area of the object"""
        return self.__size ** 2
