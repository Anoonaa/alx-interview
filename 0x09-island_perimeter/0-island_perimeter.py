#!/usr/bin/python3
"""Island perimeter computing module."""

def island_perimeter(grid):
    """
    Computes the perimeter of an island represented in a 2D grid.

    Parameters:
        grid (list of list of int): A 2D grid representing water (0) and land (1).

    Returns:
        int: The perimeter of the island.
    """
    if not isinstance(grid, list) or not all(isinstance(row, list) for row in grid):
        return 0
    
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter


