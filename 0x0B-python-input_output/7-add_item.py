#!/usr/bin/python3
"""A module that adds all arguments to a python list and then save
them to a json file"""
from sys import argv
import os


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
List = []
a = 1
try:
    os.mknod(filename)
    os.stat(filename).st_size == 0
    while a < len(argv):
        List = list(argv[a])
        a += 1
    save(List, filename)
except FileExistsError:
    List = load(filename)
    while a < len(argv):
        List.append(argv[a])
        a += 1
    save(List, filename)
