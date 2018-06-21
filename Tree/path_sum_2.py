# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# For example: Given the below binary tree and sum = 22.
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      5
# return
# [
#    [5, 4, 11, 2],
#    [5, 8, 4, 5]
# ]
from binarytree import Node


def path_sum(root, sum):
    ret = []
    if root is None:
        return ret
    curr = []
    dfs(ret, curr, sum, 0, root)
    
    return ret


def dfs(ret, curr, sum, tmpsum, root):
    if root is None:
        return

    tmpcurr = [c for c in curr]
    tmpcurr.append(root.value)
    tmpsum +=  root.value
    
    if tmpsum == sum:
        if root.left is None and root.right is None:
            ret.append(tmpcurr)
            return
    
    dfs(ret, tmpcurr, sum, tmpsum, root.left)
    dfs(ret, tmpcurr, sum, tmpsum, root.right)

if __name__ == '__main__':
    node = Node(5)
    node.left = Node(4)
    node.right = Node(8)
    node.left.left = Node(11)
    node.right.left = Node(13)
    node.right.right = Node(4)
    node.left.left.left = Node(7)
    node.left.left.right = Node(2)
    node.right.right.right = Node(5)

    print(node)

    print('sum = 22')
    print('result:')

    print(path_sum(node, 22))
