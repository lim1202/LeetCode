"""Sort"""

import random
import time

def bubble_sort(unsorted_list):
    """Bubble Sort"""
    if not unsorted_list:
        return None

    nums = unsorted_list.copy()

    for i in range(len(nums)):
        flag = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True
        if not flag:
            break
    return nums

def insertion_sort(unsorted_list):
    """Insertion Sort"""
    if not unsorted_list:
        return None

    nums = unsorted_list.copy()

    for i in range(1, len(nums)):
        value = nums[i]
        j = i - 1
        while j >= 0:
            if nums[j] > value:
                nums[j + 1] = nums[j]
            else:
                break
            j = j - 1
        nums[j + 1] = value

    return nums

if __name__ == "__main__":
    RANDOM_LIST = [i for i in range(1, 11)]
    random.shuffle(RANDOM_LIST)
    print('Test array: {}'.format(RANDOM_LIST))

    start_time = time.time()
    BS_LIST = bubble_sort(RANDOM_LIST)
    print('Bubble Sort result: {}'.format(BS_LIST))
    print('Duration: {} ms'.format((time.time() - start_time) * 1000))

    start_time = time.time()
    IS_LIST = insertion_sort(RANDOM_LIST)
    print('Insertion Sort result: {}'.format(IS_LIST))
    print('Duration: {} ms'.format((time.time() - start_time) * 1000))
