#!/usr/bin/python3
"""returns a list of lists of integers
    representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    trg = [[] for i in range(n)]

    for i in range(n):
        for j in range(i + 1):
            if (j < i):
                if (j == 0):
                    trg[i].append(1)
                else:
                    trg[i].append(trg[i - 1][j] + trg[i - 1][j - 1])
            elif (j == i):
                trg[i].append(1)
    return trg
