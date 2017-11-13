# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# For example, Given nums = [0, 1, 3] return 2.
# Note: Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?


def missing_number(nums):
    x = 0
    for i in range(len(nums) + 1):
        x ^= i
    for num in nums:
        x ^= num
    return x


if __name__ == '__main__':
    nums = [0, 1, 3]
    print('Missing number in', nums, 'is:', missing_number(nums))
