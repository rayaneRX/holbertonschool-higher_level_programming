#!/usr/bin/python3
"""function that divides all elements of a matrix."""

msg = "matrix must be a matrix (list of lists) of integers/floats"


def matrix_divided(matrix, div):
    if not all(isinstance(popo, list) for popo in matrix):
        raise TypeError(msg)
    if not all(isinstance(op, (int, float)) for popo in matrix for op in popo):
        raise TypeError(msg)
    if not all(len(row) == len(matrix[0])for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
            
    return [list(map(lambda m: round(m / div, 2), row)) for row in matrix]