'''Maximum Subarray'''
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest sum.
# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.


def max_subarray(array):
    '''Maximum subarray sum'''
    array_sum = 0
    max_sum = 0

    for item in array:
        array_sum = array_sum + item
        max_sum = max(max_sum, array_sum)

        if array_sum < 0:
            array_sum = 0

    return max_sum


if __name__ == '__main__':
    ARRAY = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print('Array:', ARRAY)
    print('Maximum subarray sum:', max_subarray(ARRAY))
