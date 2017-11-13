# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
from largest_rectangle_in_histogram import largest_rectangle


def maximal_rectangle(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    m = len(matrix)
    n = len(matrix[0])

    height = [[0 for col in range(n)] for row in range(m)]
    for i in range(m - 1):
        for j in range(n - 1):
            if matrix[i][j] == 0:
                pass
            else:
                if i == 0:
                    height[i][j] = 1
                else:
                    height[i][j] = height[i - 1][j] + 1

    maxArea = 0
    for i in range(m - 1):
        maxArea = max(maxArea, largest_rectangle(height[i]))

    return maxArea


if __name__ == '__main__':
    matrix = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 0], [0, 1, 0, 0]]
    print('Matrix:', matrix)
    print('Maximal rectangle is:', maximal_rectangle(matrix))
