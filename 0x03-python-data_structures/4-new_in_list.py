#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    for i in new_list:
        if idx < 0:
            return (new_list)
        elif idx > len(new_list) - 1:
            return (new_list)
        elif idx == new_list.index(i):
            new_list[idx] = element
            return (new_list)
