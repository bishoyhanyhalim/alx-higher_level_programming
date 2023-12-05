#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for look in matrix:
        for nice in look:
            print("{:d}".format(nice), end=" " if nice != look[-1] else "")
        print()
