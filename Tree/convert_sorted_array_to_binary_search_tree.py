# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
from binarytree import Node, show


def sorted_array_to_bst(nums):
    return build(nums, 0, len(nums))


def build(nums, start, end):
    if start >= end:
        return

    mid = (start + end) // 2

    node = Node(nums[mid])
    node.left = build(nums, start, mid)
    node.right = build(nums, mid + 1, end)

    return node


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(nums)
    show(sorted_array_to_bst(nums))
