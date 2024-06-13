#!/usr/bin/python3

""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """ Rotates 2D matrix 90 degrees clockwise """
    x = len(matrix)

    # Transposing the matrix
    for y in range(x):
        for z in range(y, x):
            matrix[y][z], matrix[z][y] = matrix[z][y], matrix[y][z]

    # Reversing each row
    for row in matrix:
        row.reverse()
