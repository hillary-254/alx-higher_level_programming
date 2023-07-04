#!/usr/bin/python3
"""A module to divides all elements of a matrix.

This module is in charge of dividing all the values of a matrix
according to a divisor given by the user. For the program to work
properly, the following aspects must be taken into account:

    * The matrix must  must be a list of lists of integers or floats.
    * Each row of the matrix must be of the same size.
    * The divisor must be a number (integer or float) other than 0.
    * The division of all elements of the matrix is rounded off
    to 2 decimal places.
    * The result is delivered in a new matrix.

"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix (:obj:`list` of :obj:`list`): The matrix to be divided.
        div (int): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with all elements divided.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
            If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    """

    list_checker(matrix)
    divisor_checker(div)

    elem_sizes = set()
    new_list = list()

    for elem in matrix:
        if list_checker(elem) is False:
            raises_matrix_type_error()

        elem_sizes = row_size_checker(elem_sizes, elem)
        values = []

        for value in elem:
            if check_for_number(value) is False:
                raises_matrix_type_error()

            values.append(round(value / div, 2))

        new_list.append(values)

    return new_list


def list_checker(value):
    """

    Checks if the value is of type list

    Args:
        value (any): The value to verify.

    Raises:
        TypeError: If `value` isn't a list.

    """

    if type(value) is not list or len(value) == 0:
        raises_matrix_type_error()


def divisor_checker(div):
    """

    Check if the divisor is integer, float or zero

    Args:
        div (any): The divisor to verify.

    Raises:
        TypeError: If `value` isn't integer or float.
        ZeroDivisionError: If `div` is equal to `0`.

    """

    if check_for_number(div) is False:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')


def check_for_number(value):
    """Check if the value is integer or float

    Args:
        value (any): The value to verify.

    Returns:
        bool: True if successful, False otherwise.

    """

    if type(value) is not int and type(value) is not float:
        return False


    if value != value:
        return False

    return True


def row_size_checker(elem_sizes, row):
    """Checks the size consistency of rows in a matrix

    Check if all rows in the matrix are inconsistently sized

    Args:
        elem_sizes (:obj:`set` of :obj:`int`): Size of each row matrix.
        row (list): A row with elements to divide.

    Returns:
        set: A unique consistent size between all rows.

    Raises:
        TypeError: If `elem_sizes` has more than one size in its contents.

    """

    elem_sizes.add(len(row))

    if len(elem_sizes) > 1:
        raise TypeError('Each row of the matrix must have the same size')

    return elem_sizes


def raises_matrix_type_error():
    """Raises a Matrix TypeError

    Raises:
        TypeError: If `matrix` list of lists of integers or floats.

    """

    raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')