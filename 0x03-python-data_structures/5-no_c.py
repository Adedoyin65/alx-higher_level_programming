#!/usr/bin/python3
def no_c(my_string):
    new = ""
    mymy = my_string
    for i in mymy:
        if i == 'c' or i == 'C':
            continue
        else:
            new += str(i)
    return (new)
