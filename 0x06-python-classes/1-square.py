#!/usr/bin/python3
"""This is a module with a class Square."""


class Square:
    """A Square class having an init method."""
    def __init__(self, size):
        """
        __init__ is the initialization method

        Args:
            size(int): The size of the square
        Note:
            No type or value verification is performed
        """
        self.__size = size

