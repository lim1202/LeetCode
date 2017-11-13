# Given an array and a value, remove all instances of that > value in place and return the new length.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.


def remove_element(numbers, elem):
    i = 0

    for number in numbers:
        if number == elem:
            continue
        numbers[i] = number
        i += 1
        
    print(numbers[0:i])
    return


if __name__ == '__main__':
    remove_element([1, 2, 2, 3, 2, 4], 2)
