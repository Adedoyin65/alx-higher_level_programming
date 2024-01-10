#!/usr/bin/python3
"""A module with a function that create an object from a json file"""
import json


def load_from_json_file(filename):
    """A function that create an object from a json file"""
    with open(filename, mode='r', encoding='utf-8') as File:
        dan = json.load(File)
