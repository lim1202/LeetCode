# Given a non-negative number represented as an array of digits, plus one to the number.
# The digits are stored such that the most significant digit is at the head of the list.


def plus_one(digits):
    numbers = list(map(int, str(digits)))

    sum = 0
    one = 1

    i = len(numbers) - 1

    while i >= 0:
        sum = one + numbers[i]
        one = sum // 10
        numbers[i] = sum % 10
        i -= 1

    if one > 0:
        numbers.insert(0, one)

    print(''.join(str(number) for number in numbers))
    return


if __name__ == '__main__':
    plus_one(999)
