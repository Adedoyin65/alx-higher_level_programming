#!/usr/bin/python3
"""A module that defines a class called Square"""


class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): Private attribute to store the size of the square.
        __position (tuple): Private attribute to store the
        position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with a specified size and position.

        Args:
            size (int): Optional. The size of the square. Defaults to 0.
            position (tuple): Optional. The position of the square.
            Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for retrieving the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position of the square.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        a = isinstance(value, tuple)
        b = len(value)
        c = all(isinstance(num, int) for num in value)
        if not a or b != 2 or not c or any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        If the position[1] is greater than 0, prints space
        before printing the square.
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
