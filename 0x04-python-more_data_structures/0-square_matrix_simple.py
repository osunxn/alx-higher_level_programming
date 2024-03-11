#!/usr/bin/python3

def square_matrix_simple(matrix):
    """
    Computes the square value of all integers of a matrix."""
    new_matrix = [[num**2 for num in row] for row in matrix]
    return new_matrix
