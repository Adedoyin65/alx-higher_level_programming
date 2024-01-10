#!/usr/bin/python3
"""A module that defines a function that returns a
python object from a json format
"""
import json


def from_json_string(my_str):
    """A function that returns a python object from a json format"""
    dan = json.loads(my_str)
    return dan
