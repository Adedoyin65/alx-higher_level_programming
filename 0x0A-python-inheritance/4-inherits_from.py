#!/usr/bin/python3
"""A module that defines a function to check if an object is an instance"""


def inherits_from(obj, a_class):
    """A function that returns True or False"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
