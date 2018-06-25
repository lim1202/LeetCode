"""Combination

Given two integers n and k, return all possible combinations of k numbers out of 1,2,...,n.
"""

def combine(n, k):

    def dfs(curr, n, k, level):
        nonlocal ret

        if len(curr) == k:
            ret.append([x for x in curr])

        if len(curr) > k:
            return

        for i in range(level, n + 1):
            curr.append(i)
            dfs(curr, n, k, i + 1)
            curr.pop()
            pass

        return


    ret = []

    if n <= 0:
        return ret
    
    curr = []
    dfs(curr, n, k, 1)

    return ret


if __name__ == '__main__':
    print('all possible combinations of 3 numbers out of 5 are:', combine(5, 3))