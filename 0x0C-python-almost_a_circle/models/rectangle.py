#!/usr/bin/python3
"""A module that defines a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """A class called Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
