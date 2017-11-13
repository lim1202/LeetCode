# Given a binary tree, flatten it to a linked list in-place.
# For example, Given
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
from binarytree import Node, tree, show


def flatten(root):
    if root is None:
        return

    f = Node(0)
    nodes = []
    nodes.append(root)

    while len(nodes):
        n = nodes.pop()
        f.right = append_right(f.right, n.value)

        if n.right is not None:
            nodes.append(n.right)

        if n.left is not None:
            nodes.append(n.left)

    return f.right


def append_right(root, val):
    if root is None:
        return Node(val)

    if root.right is None:
        root.right = Node(val)
    else:
        root.right = append_right(root.right, val)

    return root


if __name__ == '__main__':
    my_tree = tree()

    show(my_tree)

    print('Flatten...')

    show(flatten(my_tree))
