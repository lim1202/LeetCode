# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight). For example, the 32-bit integer 11 has binary representation 00000000000000000000000000001011, so the function should return 3.


def hamming_weight(num):
    count = 0

    while num > 0:
        count += num & 1
        num >>= 1

    return count


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5]
    for num in nums:
        print(num, 'has', hamming_weight(num), 'of \'1\' bits')
