"""Perfect Squares

Given a positive integer n, 
find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n. 
For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
import sys


def num_squares(n):
    dp = [sys.maxsize for i in range(n + 1)]

    dp[0] = 0

    for i in range(n + 1):
        j = 1
        while i + j * j <= n:
            dp[i + j * j] = min(dp[i + j * j], dp[i] + 1) 
            j = j + 1
            pass

    return dp[n]


def perfect_squares(n):
    dp = [sys.maxsize for i in range(n + 1)]  # the least number of perfect square numbers  
    num_list = [[1 for j in range(i)] for i in range(n + 1)]  # number list of perfect square numbers

    dp[0] = 0

    for i in range(n + 1):
        j = 1

        while i + j * j <= n:
            if i >= 0 and (dp[i + j * j] > dp[i] + 1):
                num_list[i + j * j] = num_list[i] + [j * j]
                pass

            dp[i + j * j] = min(dp[i + j * j], dp[i] + 1) 

            j = j + 1
            pass

    num_list[n].sort(reverse=True)
    return num_list[n]


if __name__ == '__main__':
    for i in range(1, 20):
        print('given n = {0}, the least number of perfect square is: {1}'.format(i, num_squares(i)))
        print('number list: {0}'.format(perfect_squares(i)))
