#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """A class Square that defines a square"""
    def __init__(self, size=0):
        """A method called __init__ with args self and size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif not size >= 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """A function that returns the square of the area"""

        return self.__size ** 2
