#!/usr/bin/python3
"""A module that defines a function that adds two number"""


def add_integer(a, b=98):
    """A function that adds to number"""
    if a is None:
        raise TypeError("a must be an integer")
    elif type(a) != str and type(b) == str:
        raise TypeError("b must be an integer")
    elif type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
        return a + b
    else:
        return a + b
