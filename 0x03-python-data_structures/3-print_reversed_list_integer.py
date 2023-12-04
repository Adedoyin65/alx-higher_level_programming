#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1
    for a in my_list[:]:
        a = my_list[i]
        print("{:d}".format(a), end="\n")
        i -= 1
