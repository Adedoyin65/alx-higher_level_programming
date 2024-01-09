#!/usr/bin/python3
"""A module that defines a function that appends"""
def append_write(filename="", text=""):
    """A function that appends a text"""
    with open(filename, mode='a', encoding='utf-8') as dan:
        line = dan.write(text)
        return line
