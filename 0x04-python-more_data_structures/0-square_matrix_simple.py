#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    return list(list(map(lambda b: b*b, numb_list)) for numb_list in matrix)
