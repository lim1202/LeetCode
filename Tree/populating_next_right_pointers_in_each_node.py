# What if the given tree could be any binary tree? Would your previous solution still work?
# Note:
# You may only use constant extra space. For example, Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL
from binarytree import tree, show


def connect(root):
    nexts = {}
    if root is None:
        return nexts

    p = root
    first = None
    last = None

    while p is not None:
        if first is None:
            if p.left is not None:
                first = p.left
            elif p.right is not None:
                first = p.right
        
        if p.left is not None:
            if last is not None:
                nexts[last.value] = p.left
            last = p.left
        
        if p.right is not None:
            if last is not None:
                nexts[last.value] = p.right
            last = p.right

        if nexts.get(p.value):
            p = nexts[p.value]
        else:
            p = first
            last = None
            first = None

    return nexts

if __name__ == "__main__":
    my_tree = tree()
    show(my_tree)
    print(connect(my_tree))