#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    k = 0
    j = 0
    while k < 3:
        for i in matrix[k][j]:
            print("{}".format(i), end=" ")
            j += 1
        k += 1
