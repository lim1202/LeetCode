# Given two binary trees, write a function to check if they are equal or not. Two binary trees are considered equal if they are structurally identical and the nodes have the same values.
from binarytree import tree


def is_same_tree(p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False

    if p.value == q.value:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, p.right)

    return False


if __name__ == '__main__':
    tree1 = tree()
    tree2 = tree()
    print('Tree A:')
    print(tree1)
    print('Tree B:')
    print(tree2)
    print('Are {0} and {1} equal? {2}'.format('Tree A', 'Tree A', is_same_tree(tree1, tree1)))
    print('Are {0} and {1} equal? {2}'.format('Tree A', 'Tree B', is_same_tree(tree1, tree2)))