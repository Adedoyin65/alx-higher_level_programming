#!/usr/bin/python3
"""A module that defines a function which create a list"""


def lookup(obj):
    """A function that returns the list of attributes and methods"""
    return list(obj.__dict__)
