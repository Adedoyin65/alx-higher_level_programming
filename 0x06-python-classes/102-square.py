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

    def __eq__(self, other):
        """
        Compares two squares for equality based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Compares two squares for inequality based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Compares if the area of the current square is
        greater than the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the current square is
            greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Compares if the area of the current square is
        greater than or equal to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the current square is
            greater than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        Compares if the area of the current square is
        less than the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the current square is
            less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Compares if the area of the current square is
        less than or equal to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the current square is
            less than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
