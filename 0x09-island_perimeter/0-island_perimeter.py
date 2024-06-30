#!/usr/bin/python3

""" Island Perimeter """

def island_perimeter(grid):
    """ Returns perimeter of island """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 1:
                perimeter += 4
                if x > 0 and grid[x - 1][y] == 1:
                    perimeter -= 2
                if y > 0 and grid[x][y - 1] == 1:
                    perimeter -= 2

    return perimeter
