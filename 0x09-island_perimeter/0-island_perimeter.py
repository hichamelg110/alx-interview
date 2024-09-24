#!/usr/bin/python3
"""Module that defines a function to calculate island perimeter."""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in a grid.

    The grid represents water as 0 and land as 1.

    Args:
        grid (list): A list of lists of integers representing an island.

    Returns:
        int: The perimeter of the island defined in the grid.
    """
    cols = len(grid[0])
    rows = len(grid)
    shared_borders = 0
    land_cells = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                land_cells += 1
                if col < cols - 1 and grid[row][col + 1] == 1:
                    shared_borders += 1
                if row < rows - 1 and grid[row + 1][col] == 1:
                    shared_borders += 1

    return land_cells * 4 - shared_borders * 2
