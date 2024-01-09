#!/usr/bin/python3
"""A module that defines a function that operate on files"""


def read_file(filename=""):
    """A function that read a file and print it in stdout"""
    with open(filename, encoding='utf-8') as dan:
        line = dan.read()
        print(line, end=" ")
