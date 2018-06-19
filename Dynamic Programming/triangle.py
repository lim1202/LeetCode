'''Triangle`'''
# Given a triangle, find the minimum path sum from top to bottom. 
# Each step you may move to adjacent numbers on the row below.
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

import sys

def minimum_total(triangle):
    row = len(triangle)
    
    if row == 0:
        return 0
    
    total = [sys.maxsize for i in range(row)]
    total[0] = triangle[0][0]

    min_total = sys.maxsize

    for i in range(1, row):
        for j in range(i, -1, -1):
            if j == 0:
                total[j] = total[j] + triangle[i][j]
            else:
                # 上一层total[i]为INT_MAX，不会影响最小值
                total[j] = min(total[j - 1], total[j]) + triangle[i][j]
    
    for i in range(0, row):
        min_total = min(min_total, total[i])

    return min_total


if __name__ == '__main__':
    my_triangle =  [
        [2, 0, 0, 0],
        [3, 4, 0, 0],
        [6, 5, 7, 0],
        [4, 1, 8, 3]
    ]
    print('Triangle:')
    for i in range(len(my_triangle)):
        print(my_triangle[i][0 : i + 1])
    print('Minimum Total is:', minimum_total(my_triangle))

