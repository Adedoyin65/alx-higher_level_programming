#!/usr/bin/python3
"""A module that defines a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """A class called Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This method returns the area of the rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """This method displays a diagram representation of the instance"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """The str method"""
        a = self.id
        b = self.x
        c = self.y
        d = self.width
        e = self.height
        return f"[Rectangle] ({a}) {b}/{c} - {d}/{e}"

    def update(self, *args, **kwargs):
        """A method that assigns an argument to each attribute"""
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            elif len(args) == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
        else:
            self.id = id
            self.width = width
            self.height = height
            self.x = x
            self.y = y
