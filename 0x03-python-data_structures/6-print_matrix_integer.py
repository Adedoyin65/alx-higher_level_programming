#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    k = 0
    for i in matrix:
        for a in matrix[k]:
            print(a, end="")
            k += 1
