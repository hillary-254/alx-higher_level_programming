#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for rows in matrix:
            x = 1
            for row in rows:
                if x == len(rows):
                    print("{:d}".format(row), end="")
                else:
                    print("{:d}".format(row), end=" ")
                x += 1
            print()
