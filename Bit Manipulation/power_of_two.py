# Given an integer, write a function to determine if it is a power of two.


def is_power_of_two(num):
    if num < 0:
        return False

    hasOne = False

    while num > 0:
        if num & 1:
            if hasOne:
                return False
            else:
                hasOne = True
        num >>= 1

    return hasOne


if __name__ == '__main__':
    nums = [2, 3, 4, 8, 12, 16, 24, 32]
    for num in nums:
        print('Is', num, 'a power of two?', is_power_of_two(num))
