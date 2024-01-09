#!/usr/bin/python3
"""A module with a function that checks for instance"""


def is_same_class(obj, a_class):
    """A function that checks an instance"""
    if type(obj) is a_class:
        return True
    else:
        return False
