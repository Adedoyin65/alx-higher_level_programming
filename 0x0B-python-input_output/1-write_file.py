#!/usr/bin/python3
"""A module that defines a function that reads a file"""


def write_file(filename="", text=""):
    """A function that writes a file and returns the number of character"""
    with open(filename, mode='w', encoding='utf-8') as dan:
        line = dan.write(text)
        return line
