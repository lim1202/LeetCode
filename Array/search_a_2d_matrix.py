# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right. The first integer of each row is greater than the last integer of the previous row. For example,
# Consider the following matrix:
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]


def search_matrix(matrix, target):
    # we set the corner case as below:
    # 1. if the row number of input matrix is 0, we set it false
    # 2. if the colomun number of input matrix is 0, we set it false
    if len(matrix) == 0:
        return False
    elif len(matrix[0]) == 0:
        return False
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1
        else:
            return True
    return False


if __name__ == '__main__':
    matrix = [[1,   3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]]
    print('Matrix is:', matrix)
    print('Is 12 in matrix?', search_matrix(matrix, 12))
    print('Is 16 in matrix?', search_matrix(matrix, 16