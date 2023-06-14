#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Creates a new matrix with the same size as the input matrix
    new_matrix = []
    # checks if matrix is not empty
    size = len(matrix)
    if size > 0:
        for rows in matrix[:]:
            new_matrix.append(list(map(lambda x: x ** 2, rows)))
    return new_matrix
