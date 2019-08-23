"""Sort"""

import random
import time


def bubble_sort(nums):
    """Bubble Sort"""
    if not nums:
        return None

    for i in range(len(nums)):
        flag = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True
        if not flag:
            break
    return


def insertion_sort(nums):
    """Insertion Sort"""
    if not nums:
        return None

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

    return


def merge_sort(nums):
    """Merge Sort"""
    if not nums:
        return None

    def merge(C, p, q, r):
        A = C[p:q+1]
        B = C[q+1:r+1]
        i = r
        j = len(A) - 1
        k = len(B) - 1

        while i >= p:
            if (j >= 0 and k >= 0):
                if A[j] > B[k]:
                    C[i] = A[j]
                    j -= 1
                else:
                    C[i] = B[k]
                    k -= 1
            elif j >= 0:
                C[i] = A[j]
                j -= 1
            elif k >= 0:
                C[i] = B[k]
                k -= 1
            i -= 1

        return

    def merge_sort_c(C, p, r):
        if p >= r:
            return

        q = (p+r)//2

        merge_sort_c(C, p, q)
        merge_sort_c(C, q+1, r)
        merge(C, p, q, r)

        return

    merge_sort_c(nums, 0, len(nums)-1)

    return


if __name__ == "__main__":
    RANDOM_LIST = [i for i in range(1, 11)]
    random.shuffle(RANDOM_LIST)
    print('Test array: {}'.format(RANDOM_LIST))

    BS_LIST = RANDOM_LIST.copy()
    start_time = time.time()
    bubble_sort(BS_LIST)
    print('Bubble Sort result: {}'.format(BS_LIST))
    print('Duration: {} ms'.format((time.time() - start_time) * 1000))

    IS_LIST = RANDOM_LIST.copy()
    start_time = time.time()
    insertion_sort(IS_LIST)
    print('Insertion Sort result: {}'.format(IS_LIST))
    print('Duration: {} ms'.format((time.time() - start_time) * 1000))

    MS_LIST = RANDOM_LIST.copy()
    start_time = time.time()
    merge_sort(MS_LIST)
    print('Merge Sort result: {}'.format(MS_LIST))
    print('Duration: {} ms'.format((time.time() - start_time) * 1000))
