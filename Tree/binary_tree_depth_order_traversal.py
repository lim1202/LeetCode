'''Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.
For example: Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].
Note: Recursive solution is trivial, could you do it iteratively?
'''
from binarytree import tree


def preorder_traversal(root):
    vals = []

    if root is None:
        return vals

    nodes = []
    nodes.append(root)

    while len(nodes):
        n = nodes.pop()
        vals.append(n.value)

        if n.right is not None:
            nodes.append(n.right)

        if n.left is not None:
            nodes.append(n.left)

    return vals


def inorder_traversal(root):
    vals = []

    if root is None:
        return vals

    nodes = []
    p = root
    while p or len(nodes):
        while p:
            nodes.append(p)
            p = p.left

        if len(nodes):
            p = nodes.pop()
            vals.append(p.value)
            p = p.right

    return vals


def postorder_traversal(root):
    vals = []

    if root is None:
        return vals

    nodes = []
    pre = None
    nodes.append(root)

    while len(nodes):
        p = nodes.pop()

        if (p.left is None and p.right is None) or (pre is not None and (pre == p.left or pre == p.right)):
            vals.append(p.value)
            pre = p
        else:
            nodes.append(p)
            if p.right is not None:
                nodes.append(p.right)

            if p.left is not None:
                nodes.append(p.left)

    return vals


if __name__ == "__main__":
    my_tree = tree()
    print(my_tree)

    print('Preorder traversal:', preorder_traversal(my_tree))
    print('Inorder traversal:', inorder_traversal(my_tree))
    print('Postorder traversal:', postorder_traversal(my_tree))
