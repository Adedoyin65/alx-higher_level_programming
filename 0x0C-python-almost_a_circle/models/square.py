#!/usr/bin/python3
"""A module that defines a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class called Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloads the __str__ method to return the desired string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size - sets both width and height"""
        self.width = value
        self.height = value
