# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
import sys
from binarytree import tree


def max_depth(root):
    if not root:
        return 0

    num = 0

    def travel(node, level):
        nonlocal num

        if node.left is None and node.right is None:
            num = max(num, level)
            return

        if node.left:
            travel(node.left, level + 1)

        if node.right:
            travel(node.right, level + 1)

    travel(root, 1)
    return num


def min_depth(root):
    if not root:
        return 0

    num = sys.maxsize

    def travel(node, level):
        nonlocal num

        if node.left is None and node.right is None:
            num = min(num, level)
            return

        if node.left:
            travel(node.left, level + 1)

        if node.right:
            travel(node.right, level + 1)

    travel(root, 1)
    return num


if __name__ == '__main__':
    # Generate a random binary tree and return its root
    my_tree = tree()
    print(my_tree)
    print('Max depth: {0}'.format(max_depth(my_tree)))
    print('Min depth: {0}'.format(min_depth(my_tree)))
