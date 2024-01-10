#!/usr/bin/python3
"""A module that defines a function that writes an object to a text file
using json representation"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes an object to a text file in json format"""
    with open(filename, mode='w', encoding='utf-8') as File:
        dan = json.dump(my_obj, File)
