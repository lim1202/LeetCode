"""Sort"""

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

if __name__ == "__main__":
    TEST_LIST = [3, 5, 4, 1, 2, 6]
    print('Test array: {}'.format(TEST_LIST))

    BS_LIST = bubble_sort(TEST_LIST)
    print('Bubble Sort result: {}'.format(BS_LIST))
