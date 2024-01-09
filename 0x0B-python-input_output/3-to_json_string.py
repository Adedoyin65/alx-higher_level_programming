#!/usr/bin/python3
"""A module that defines a function that returns json format of an object"""
import json

def to_json_string(my_obj):
    """A function that returns json representation of an object"""
    return json.dumps(my_obj)
