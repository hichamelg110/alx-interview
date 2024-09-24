#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    This function uses a unique approach by counting the number of land-water
    transitions in both horizontal and vertical directions.

    Args:
    grid : A 2D grid where 0 represents water and 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check left edge
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check right edge
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1
                # Check top edge
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check bottom edge
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1

    return perimeter

