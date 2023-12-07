#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nl = my_list.copy()
    for i in my_list:
        if i == search:
            nl[nl.index(i)] = replace
        else:
            continue
    return (nl)
