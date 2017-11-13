# Given a sorted array, remove the duplicates in place such that > each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# For example, Given input array A = [1,1,2],
# Your function should return length = 2, and A is now [1,2].


def remove_duplicates(numbers):
    i = 0
    
    for number in numbers:
        if numbers[i] != number:
            i += 1
            numbers[i] = number

    print(numbers[0:i + 1])
    return


if __name__ == '__main__':
    remove_duplicates([1, 1, 2])
