#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    hellos = []
    for col in matrix:
        result = list(map(lambda x: x**2, col))
        hellos.append(result)

    return (hellos)
