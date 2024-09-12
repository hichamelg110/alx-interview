#!/usr/bin/python3
""" Module for rotating a 2D matrix
"""

def rotate_2d_matrix(matrix):
    """ Rotates an n x n 2D matrix 90 degrees clockwise in-place
    Args:
        matrix (list of lists): The input matrix to be rotated
    """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_2d_matrix(matrix)
    print(matrix)
