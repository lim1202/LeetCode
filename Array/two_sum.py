# Given an array of intergers, find two numbers such that they add up to a specific target number. The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2 Please note that your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution.
# Input: numbers={2, 7, 11, 15}, target=9 Output: index1=1, index2=2

def two_sum(numbers, target):
    for i in range(len(numbers) - 1):
        ret = [0, 0]
        rest_val = target - numbers[i]
        if rest_val in numbers:
            index = numbers.index(rest_val)
            if index == i:
                continue
            elif index < i:
                ret = [index + 1, i + 1]
                break
            elif index > i:
                ret = [i + 1, index + 1]
                break
        
    print(ret)
    return

if __name__ == '__main__':
    two_sum([2, 7, 11, 15], 9)