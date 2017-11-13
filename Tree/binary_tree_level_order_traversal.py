from binarytree import tree, show


# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
# For example: Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
def level_order(node):

    def dfs(node, level):
        nonlocal ret

        if node is None:
            return

        ret[level].append(node.value)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
        return

    height = get_height(node)
    ret = [[] for i in range(height)]

    if height == 0:
        return ret

    dfs(node, 0)
    return ret


# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (from left to right, level by level from leaf to root)
# For example: Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
def level_order_bottom_up(node):

    def dfs(node, level):
        nonlocal ret

        if node is None:
            return

        ret[level].append(node.value)
        dfs(node.left, level - 1)
        dfs(node.right, level - 1)
        return

    height = get_height(node)
    ret = [[] for i in range(height)]

    if height == 0:
        return ret

    dfs(node, height - 1)
    return ret


# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
# For example: Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
def level_order_zigzag(node):

    def dfs(node, level):
        nonlocal ret

        if node is None:
            return

        ret[level].append(node.value)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
        return

    height = get_height(node)
    ret = [[] for i in range(height)]

    if height == 0:
        return ret

    dfs(node, 0)

    for i in range(height):
        if i % 2:
            ret[i].reverse()

    return ret


def get_height(node):
    if node is None:
        return 0

    left = get_height(node.left)
    right = get_height(node.right)

    if left > right:
        height = left + 1
    else:
        height = right + 1

    return height


if __name__ == "__main__":
    my_tree = tree()
    show(my_tree)

    print('Level order:')
    orders = level_order(my_tree)
    for order in orders:
        print(order)

    print('Level order bottom-up:')
    orders = level_order_bottom_up(my_tree)
    for order in orders:
        print(order)

    print('Level order zigzag:')
    orders = level_order_zigzag(my_tree)
    for order in orders:
        print(order)