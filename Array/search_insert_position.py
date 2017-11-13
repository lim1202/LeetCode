# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0


def search_insert(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low


if __name__ == '__main__':
    array = [1, 3, 5, 6]
    print('Array:', array)
    targets = [5, 2, 7, 0]
    for target in targets:
        print(target, '→', search_insert(array, target))
