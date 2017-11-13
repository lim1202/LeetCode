# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
# For example, Given height = [2,1,5,6,2,3], return 10.


def largest_rectangle(height):
    s = []
    height.append(0)
    sum = 0
    i = 0
    while i < len(height):
        if len(s) == 0 or height[i] > height[s[-1]]:
            s.append(i)
            i += 1
        else:
            t = s.pop()
            if len(s) == 0:
                width = i
            else:
                width = i - 1 - s[-1]
            sum = max(sum, height[t] * width)

    return sum


if __name__ == '__main__':
    height = [2, 1, 5, 6, 2, 3]
    print('Largest rectangle in histogram ',
      height, ' is:', largest_rectangle(height))
