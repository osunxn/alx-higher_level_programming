#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

'''if not matrix:'''
if len(matrix) == 0 or all(len(sublist) == 0 for sublist in matrix):
    print("The matrix is empty")
else:
    print("The matrix is not empty")
