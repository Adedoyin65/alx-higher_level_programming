#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in my_list:
        if i == search:
            idx = my_list.index(i)
            my_list[idx] = replace
            new = my_list
            return (new)
        else:
            continue
