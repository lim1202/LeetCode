"""Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
from binarytree import Node, tree


def is_balanced(root):
    if root is None:
        return True

    if get_height(root) == -1:
        return False
    else:
        return True

    
def get_height(root):
    if root is None:
        return 0

    left_height = get_height(root.left)
    if left_height == -1:
        return -1

    right_height = get_height(root.right)
    if right_height == -1:
        return -1

    diff_height = abs(right_height - left_height)
    if diff_height > 1:
        return -1
    else:
        return max(left_height, right_height) + 1


if __name__ == "__main__":
    my_tree = tree()
    print(my_tree)
    print('Is tree balanced?', is_balanced(my_tree))

    node = Node(0)
    node.left = Node(1)
    node.right = Node(2)
    node.left.left = Node(3)
    node.left.right = Node(4)
    node.right.left = Node(5)
    node.right.right = Node(6)
    print(node)
    print('Is tree balanced?', is_balanced(node))
