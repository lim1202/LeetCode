# Given numRows, generate the first numRows of Pascal's triangle.
# For example, given numRows = 5, Return
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

# Given an index k, return the kth row of the Pascal's triangle.
# For example, given k = 3, Return [1,3,3,1].


def get_row(index):
    vals = [1 for i in range(index + 1)]

    for i in range(index + 1):
        j = i - 1
        while j >= 1:
            vals[j] = vals[j] + vals[j - 1]
            j -= 1

    print(vals)
    return


if __name__ == '__main__':
    get_row(0)
    get_row(1)
    get_row(2)
    get_row(3)
    get_row(4)
