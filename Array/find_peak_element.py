# A peak element is an element that is greater than its neighbors.
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that num[-1] = num[n] = -∞.
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.


def find_peak_element(numbers):
    n = len(numbers)
    if n == 1:
        return 0

    start = 0
    end = n - 1
    mid = 0

    while start <= end:
        mid = start + (end - start) // 2
        if (mid == 0 or numbers[mid] >= numbers[mid - 1]) and (mid == n - 1 or numbers[mid] >= numbers[mid + 1]):
            return mid
        elif mid > 0 and numbers[mid] < numbers[mid - 1]:
            end = mid - 1
        else:
            start = mid + 1

    return mid


if __name__ == '__main__':
    array = [1, 2, 3, 1]
    print('Pear elements in array', array, 'are:', find_peak_element(array))
