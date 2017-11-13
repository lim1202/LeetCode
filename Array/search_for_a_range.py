# Given a sorted array of integers, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].


def search_range(numbers, target):
    result = [-1, -1]
    if len(numbers) == 0:
        return result

    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if numbers[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1

    if low < len(numbers) and numbers[low] == target:
        result[0] = low
    else:
        return result

    high = len(numbers) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if numbers[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1

    result[1] = high

    return result


if __name__ == '__main__':
    array = [5, 7, 7, 8, 8, 10]
    target = 8
    print('The range of', target, 'in array',
          array, 'is:', search_range(array, target))
