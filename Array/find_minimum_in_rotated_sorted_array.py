# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
# The array may contain duplicates.


def find_min(numbers):
    size = len(numbers)
    if size == 0:
        return 0
    elif size == 1:
        return numbers[0]
    elif size == 2:
        return min(numbers[0], numbers[1])

    start = 0
    stop = size - 1

    while start < stop - 1:
        if numbers[start] < numbers[stop]:
            return numbers[start]

        mid = start + (stop - start) // 2
        if numbers[mid] > numbers[start]:
            start = mid
        elif numbers[mid] < numbers[start]:
            stop = mid
        else:
            start += 1

    return min(numbers[start], numbers[stop])


if __name__ == '__main__':
    print('Minimum number in [4,5,6,7,0,1,2] is',
          find_min([4, 5, 6, 7, 0, 1, 2]))
    print('Minimum number in [7,0,1,2,4,5,6] is',
          find_min([7, 0, 1, 2, 4, 5, 6]))
    print('Minimum number in [7,2,4,4,4,5,6] is',
          find_min([7, 2, 4, 4, 4, 5, 6]))
