#!/usr/bin/env python3
from typing import Optional, List, Union
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root: Optional[TreeNode]):
    if not root:
        return

    queue = deque([root])
    result = []
    while queue:
        # print(queue[0].val)
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


# Valid by assuming for a balanced BST. meaning None parents has none childre
# def toBinaryTree(nums: List) -> Optional[TreeNode]:
#     if not nums:
#         return None

#     def BinaryTree(level) -> Union[None, TreeNode]:
#         if level >= len(nums) or nums[level] == None:
#             return None

#         node = TreeNode(nums[level])
#         node.left = BinaryTree((2 * level) + 1)
#         node.right = BinaryTree((2 * level) + 2)

#         return node

#     head = BinaryTree(0)

#     return head


def toBinaryTree(nums: List) -> Optional[TreeNode]:
    if not nums:
        return None

    root = TreeNode(nums[0])
    queue = deque([root])
    idx = 1

    while queue and idx < len(nums):
        node = queue.popleft()
        if nums[idx]:
            newNode = TreeNode(nums[idx])
            node.left = newNode
            queue.append(newNode)
        idx += 1
        if idx < len(nums) and nums[idx]:
            newNode = TreeNode(nums[idx])
            node.right = newNode
            queue.append(newNode)

        idx += 1

    return root
