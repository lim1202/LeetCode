# Given two sorted integer arrays A and B, merge B into A as one sorted array.
# Note: You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.


def merge_sorted_array(A, B):
    m = len(A)
    n = len(B)
    C = [0 for i in range(m + n)]

    i = m + n - 1
    j = m - 1
    k = n - 1

    while i >= 0:
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

    print('A:', A)
    print('B:', B)
    print('Result:', C)
    return


if __name__ == '__main__':
    merge_sorted_array([1, 2, 5], [3, 4])
