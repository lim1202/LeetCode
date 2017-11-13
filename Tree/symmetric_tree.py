# Given a binary tree, check whether it is a mirror of itself(ie, symmetric around its center)
# For example, this tree is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following tree is not.
#     1
#    / \
#   2   2
#    \   \
#    3    3
from binarytree import Node, tree, show


def is_symmetric(root):
    if root is None:
        return True

    return helper(root.left, root.right)


def helper(left, right):
    if left is None and right is None:
        return True
    elif left is None or right is None:
        return False
    
    cond1 = left.value == right.value
    cond2 = helper(left.left, right.right)
    cond3 = helper(left.right, right.left)

    return cond1 and cond2 and cond3


if __name__ == '__main__':
    node1 = Node(1)
    node1.left = Node(2)
    node1.right = Node(2)
    node1.left.left = Node(3)
    node1.left.right = Node(4)
    node1.right.left = Node(4)
    node1.right.right = Node(3)
    show(node1)
    print('Is symmetric?', is_symmetric(node1))

    node2 = Node(1)
    node2.left = Node(2)
    node2.right = Node(2)
    node2.left.right = Node(3)
    node2.right.right = Node(3)
    show(node2)
    print('Is symmetric?', is_symmetric(node2))

