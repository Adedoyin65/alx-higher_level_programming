#!/usr/bin/python3
"""A module that defines a class called Square"""


class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): Private attribute to store the size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with a specified size.

        Args:
            size (int): Optional. The size of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character # to stdout.

        If the size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
