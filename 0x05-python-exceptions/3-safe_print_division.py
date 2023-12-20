#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return (a/b)
    except ZeroDivisionError:
        return (None)
    finally:
        if b == 0:
            res = None
        else:
            res = a/b
        print("Inside result: {}".format(res))
