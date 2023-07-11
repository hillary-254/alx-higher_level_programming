#!/usr/bin/python3
"""
Module that generate Pascal's triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to level n.

    Args:
        n (int): The level of Pascal's triangle to generate.

    Returns:
        list: List of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)
        triangle.append(row)

    return triangle
