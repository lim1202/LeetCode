"""Binary Tree Path

Given a binary tree, return all root-to-leaf paths.
For example, given the following binary tree:
   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:
["1->2->5", "1->3"]
"""
from binarytree import tree


def binary_tree_paths(root):
    """Return all root-to-leaf paths"""
    result = []

    if root is None:
        return result

    path = []
    dfs(root, path, result)
    return result


def dfs(node, path, result):
    """Iterator, Depth-First-Search"""
    if node is None:
        return

    path.append(node.value)

    if node.left is None and node.right is None:
        result.append(generate_path(path))
    else:
        if node.left is not None:
            dfs(node.left, path, result)
            path.pop()
        if node.right is not None:
            dfs(node.right, path, result)
            path.pop()

def generate_path(paths):
    """Generate path string from path list"""
    path_str = ""

    for path in paths:
        if path_str == "":
            path_str = str(path)
        else:
            path_str += "->" + str(path)

    return path_str


if __name__ == "__main__":
    MY_TREE = tree()
    print(MY_TREE)
    print(binary_tree_paths(MY_TREE))
