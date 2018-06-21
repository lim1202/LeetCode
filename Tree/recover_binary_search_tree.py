"""Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Note:
    A solution using O(n) space is pretty straight forward.
    Could you devise a constant space solution?
"""
from binarytree import build


def recover_tree(root):
    """Recover the binary search tree"""
    found = False
    pre_cur = None
    pre1 = None
    pre2 = None

    if root is None:
        return

    cur = root
    while cur is not None:
        if cur.left is None:
            if pre_cur and pre_cur.value > cur.value:
                if not found:
                    pre1 = pre_cur
                    found = True
                pre2 = cur

            pre_cur = cur
            cur = cur.right
        else:
            pre = cur.left
            while pre.right and pre.right.value != cur.value:
                pre = pre.right
            if pre.right is None:
                pre.right = cur
                cur = cur.left
            else:
                if pre_cur.value > cur.value:
                    if not found:
                        pre1 = pre_cur
                        found = True
                    pre2 = cur
                pre_cur = cur
                pre.right = None
                cur = cur.right

        if pre1 and pre2:
            temp = pre1.value
            pre1.value = pre2.value
            pre2.value = temp

    return

if __name__ == "__main__":
    my_tree = build([4, 2, 7, 1, 3, 6, 5])
    print(my_tree)
    recover_tree(my_tree)
    print(my_tree)
