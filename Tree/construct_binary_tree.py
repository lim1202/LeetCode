# Given preorder and inorder traversal of a tree, construct the binary tree.
# Given inorder and postorder traversal of a tree, construct the binary tree.
from binarytree import Node, tree, show


def build_tree(inorder, preorder=None, postorder=None):
    if preorder is not None:
        return build_inorder_preorder(inorder, 0, len(inorder) - 1, preorder, 0, len(preorder) - 1)
    elif postorder is not None:
        return build_inorder_postorder(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)
    else:
        return


def build_inorder_preorder(inorder, s0, e0, preorder, s1, e1):
    if s0 > e0 or s1 > e1:
        return

    root = Node(preorder[s1])

    mid = inorder.index(preorder[s1])
    num = mid - s0

    root.left = build_inorder_preorder(
        inorder, s0, mid - 1, preorder, s1 + 1, s1 + num)
    root.right = build_inorder_preorder(
        inorder, mid + 1, e0, preorder, s1 + num + 1, e1)

    return root


def build_inorder_postorder(inorder, s0, e0, postorder, s1, e1):
    if s0 > e0 or s1 > e1:
        return

    root = Node(postorder[e1])

    mid = inorder.index(postorder[e1])
    num = mid - s0

    root.left = build_inorder_postorder(
        inorder, s0, mid - 1, postorder, s1, s1 + num - 1)
    root.right = build_inorder_postorder(
        inorder, mid + 1, e0, postorder, s1 + num, e1 - 1)

    return root


if __name__ == '__main__':
    show(build_tree([4, 2, 5, 1, 6, 3, 7], None,  [4, 5, 2, 6, 7, 3, 1]))
    show(build_tree([4, 2, 1, 5, 3, 6, 7], None, [4, 2, 5, 7, 6, 3, 1]))
    show(build_tree([4, 5, 2, 6, 1, 3, 7], None, [4, 5, 6, 2, 7, 3, 1]))
    show(build_tree([4, 2, 5, 1, 6, 3, 7], [1, 2, 4, 5, 3, 6, 7]))
    show(build_tree([4, 2, 1, 5, 3, 6, 7], [1, 2, 4, 3, 5, 6, 7]))
    show(build_tree([4, 5, 2, 6, 1, 3, 7], [1, 2, 5, 4, 6, 3, 7]))
