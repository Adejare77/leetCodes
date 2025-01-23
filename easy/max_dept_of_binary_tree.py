#!/usr/bin/env python3

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Using Depth First Search
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         def max_depth(root: Optional[TreeNode], count:int, depth: int):
#             if not root:
#                 return max(count, depth)

#             count += 1
#             farthest_leaf = max_depth(root.left, count, depth)
#             farthest_leaf = max_depth(root.right, count, farthest_leaf)

#             return max(count, farthest_leaf)

#         return max_depth(root, 0, 0)

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         left_depth = self.maxDepth(root.left)
#         right_depth = self.maxDepth(root.right)

#         return 1 + max(left_depth, right_depth)


# Using Breadth First Search
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        max_depth = 0

        while queue:
            root, depth = queue.popleft()
            max_depth = depth

            if root.left:
                queue.append((root.left, depth + 1))

            if root.right:
                queue.append((root.right, depth + 1))

        return max_depth
