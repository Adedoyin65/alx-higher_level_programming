#!/usr/bin/python3
def no_c(my_string):
    mymy = my_string
    for i in mymy:
        if i == 'c' or i == 'C':
            continue
        else:
            new = ""
            new += i
            return (new)
