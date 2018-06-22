r"""Unique Binary Search Trees

Given n, how many structurally unique BSTs (binary search trees) that store values 1...n?
For example, Given n = 3, there are a total of 5 unique BSTs.
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
from binarytree import Node


def num_trees(n):
    if n == 0:
        return 0

    dp = [0 for i in range(n+1)]
    
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            # 如果左子树的个数为j，那么右子树为i - j - 1
            dp[i] = dp[i] + dp[j] * dp[i - j - 1]
            pass

    return dp[n]

r"""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
For example, Given n = 3, your program should return all 5 unique BST's shown below.
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
def generate_trees(n):
    return generate(1, n)


def generate(start, stop):
    vs = []

    if start > stop:
        # 没有子树了，返回null
        vs.append(None)
        return vs

    for i in range(start, stop + 1):
        left_list = generate(start, i - 1)
        right_list = generate(i + 1, stop)

        # 获取左子树和右子树所有排列之后，放到root为i的节点的下面
        for j in range(len(left_list)):
            for k in range(len(right_list)):
                node = Node(i)
                node.left = left_list[j]
                node.right = right_list[k]
                vs.append(node)

    return vs

if __name__ == '__main__':
    for i in range(1, 10):
        print('Given n = {0}, there are a total of {1} unique BST''s.'.format(i, num_trees(i)))
        pass

    print('Given n = 3, return all 5 unique BST''s shown below')
    nodes = generate_trees(3)
    for node in nodes:
        print(node)
        pass



    