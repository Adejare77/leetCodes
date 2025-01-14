#!/usr/bin/env python3
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True
        def checkHeight(root: Optional[TreeNode]):
            nonlocal result
            if not root:
                return 0

            left = checkHeight(root.left)
            right = checkHeight(root.right)

            if (abs(left - right)) > 1:
                result = False
                return 0

            return 1 + max(left, right)

        checkHeight(root)

        return result




from collections import deque

def createTree(level_order):
    if not level_order:
        return None

    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1

    while queue and i < len(level_order):
        current = queue.popleft()

        if level_order[i] is not None:
            current.left = TreeNode(level_order[i])
            queue.append(current.left)
        i += 1

        if i < len(level_order) and level_order[i] is not None:
            current.right = TreeNode(level_order[i])
            queue.append(current.right)
        i += 1

    return root

level_order = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]
root = createTree(level_order)

print(Solution().isBalanced(root))

# def printTree(root: Optional[TreeNode]):
#     if not root:
#         return "Nothing in this Tree"

#     queue = deque([root])

#     while queue:
#         root, queue = queue.popleft()
#         print(root.val)
