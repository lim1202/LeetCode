"""Sum Root to Leaf Numbers"""
# Given a binary tree containing digits from 0-9 only,
# each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers. For example,
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Return the sum = 12 + 13 = 25.
from binarytree import convert, show

def sum_numbers(root):
    """Return sum of all root-to-leaf numbers"""
    arr = []
    total = 0

    def dfs(node, arr):
        """Depth-First-Search"""
        nonlocal total
        if node is None:
            return

        arr.append(node.value)

        if node.left is None and node.right is None:
            num = vec2num(arr)
            total = total + num
        else:
            if node.left is not None:
                dfs(node.left, arr)
            if node.right is not None:
                dfs(node.right, arr)

        arr.pop()

    dfs(root, arr)
    return total


def vec2num(vec):
    """Convert list to number"""
    num = 0
    for node in vec:
        num = num * 10 + node
    return num


if __name__ == '__main__':
    MY_TREE = convert([1, 2, 3, 4, 5, 6, 7])
    show(MY_TREE)
    print("sum:", sum_numbers(MY_TREE))
