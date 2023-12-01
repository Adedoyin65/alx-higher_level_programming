#!/usr/bin/python3
from sys import argv
a = 1
if len(argv) == 1:
    print("{} arguments.".format(len(argv) - 1))
elif len(argv) == 2:
    print("{} argument:".format(len(argv) - 1))
    for i in argv[1:]:
        print("{}: {}".format(a, i), end="\n")
        a += 1
elif len(argv) > 2:
    print("{} arguments:".format(len(argv) - 1))
    for i in argv[1:]:
        print("{}: {}".format(a, i), end="\n")
        a += 1
