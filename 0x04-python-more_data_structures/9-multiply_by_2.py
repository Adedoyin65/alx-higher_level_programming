#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    s = a_dictionary.copy()
    for k, v in s.items():
        if k in s:
            s[k] = 2 * v
    return (s)
