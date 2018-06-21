"""Validate Binary Search Tree"""
# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
import sys
from binarytree import build

def is_valid_bst(root):
    """Return is a valid BST"""
    return valid(root, 0, sys.maxsize)


def valid(node, min_value, max_value):
    """Iteratively validate BST"""
    if node is None:
        return True

    if node.value <= min_value or node.value >= max_value:
        return False

    return valid(node.left, min_value, node.value) and valid(node.right, node.value, max_value)


if __name__ == '__main__':
    TREE1 = build([7, 3, 2, 6, 9, 4, 1])
    print(TREE1)
    print("Is a valid binary search tree?", is_valid_bst(TREE1))
    TREE2 = build([4, 2, 6, 1, 3, 5, 7])
    print(TREE2)
    print("Is a valid binary search tree?", is_valid_bst(TREE2))
