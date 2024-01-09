#!/usr/bin/python3
"""A module to check if an object is an instance"""
def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
