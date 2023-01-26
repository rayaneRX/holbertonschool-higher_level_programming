#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        row = []
        for val in i:
            row.append(val**2)
        new_matrix.append(row)
    return new_matrix


'''
return[list(map(lambda val: val**2, row))for row in matrix]
'''
