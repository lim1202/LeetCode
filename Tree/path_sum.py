# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# For example: Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
from binarytree import Node, show


def has_path_sum(root, sum):
    if root is None:
        return False

    return dfs(sum, 0, root)


def dfs(target, sum, root):
    if root is None:
        return False

    sum += root.value
    if root.left is None and root.right is None:
        if sum == target:
            return True
        else:
            return False

    left_part = dfs(target, sum, root.left)
    right_part = dfs(target, sum, root.right)
    return left_part or right_part


if __name__ == '__main__':
    node = Node(5)
    node.left = Node(4)
    node.right = Node(8)
    node.left.left = Node(11)
    node.right.left = Node(13)
    node.right.right = Node(4)
    node.left.left.left = Node(7)
    node.right.right.right = Node(1)

    show(node)

    print('Exist a root-to-leaf path which sum is 22?', has_path_sum(node, 22))
    print('Exist a root-to-leaf path which sum is 27?', has_path_sum(node, 27))
