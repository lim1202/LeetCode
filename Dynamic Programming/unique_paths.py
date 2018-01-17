'''Unique Paths'''
# Unique Path
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid
# (marked 'Finish' in the diagram below).
# How many possible unique paths are there?


def unique_paths(cols, rows):
    '''Unique paths'''
    dp_list = [[1 for i in range(cols)] for i in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            dp_list[i][j] = dp_list[i - 1][j] + dp_list[i][j - 1]

    return dp_list[rows - 1][cols - 1]


# Unique Path II
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.


def unique_paths_with_obstacles(grid):
    '''Unique path with obstacles'''
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    dp_list = [[1 for i in range(cols)] for i in range(rows)]

    dp_list[0][0] = 1 if grid[0][0] == 0 else 0

    for i in range(1, rows):
        dp_list[i][0] = 1 if dp_list[i - 1][0] == 1 and grid[i][0] == 0 else 0

    for j in range(1, cols):
        dp_list[0][j] = 1 if dp_list[0][j - 1] == 1 and grid[0][j] == 0 else 0

    for i in range(1, rows):
        for j in range(1, cols):
            if grid[i][j] == 0:
                dp_list[i][j] = dp_list[i - 1][j] + dp_list[i][j - 1]
            else:
                dp_list[i][j] = 0

    return dp_list[rows - 1][cols - 1]


# Minimum Path Sum
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.


def min_path_sum(grid):
    '''Minimum path sum'''
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    dp_list = [[1 for i in range(cols)] for i in range(rows)]

    dp_list[0][0] = grid[0][0]

    for i in range(1, rows):
        dp_list[i][0] = dp_list[i - 1][0] + grid[i][0]

    for j in range(1, cols):
        dp_list[0][j] = dp_list[0][j - 1] + grid[0][j]

    for i in range(1, rows):
        for j in range(1, cols):
            dp_list[i][j] = min(dp_list[i - 1][j], dp_list[i][j - 1]) + grid[i][j]

    return dp_list[rows - 1][cols - 1]


if __name__ == '__main__':
    print('Unique paths')
    print('2 x 2:', unique_paths(2, 2))
    print('3 x 3:', unique_paths(3, 3))
    print('3 x 4:', unique_paths(3, 4))
    print('4 x 4:', unique_paths(4, 4))
    print('Unique paths with obstacles')
    GRID2 = [[0, 1], [0, 0]]
    print('grid:', GRID2)
    print('paths:', unique_paths_with_obstacles(GRID2))
    GRID3 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print('grid:', GRID3)
    print('paths:', unique_paths_with_obstacles(GRID3))
    print('Minimum path sum')
    GRID22 = [[0, 1], [2, 3]]
    print('grid:', GRID22)
    print('sum:', min_path_sum(GRID22))
