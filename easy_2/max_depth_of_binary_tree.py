#!/usr/bin/env python3

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         def recursive_max_depth(current, q: Optional[TreeNode]):
#             if not q:
#                 return current

#             return max(recursive_max_depth(current + 1, q.left), recursive_max_depth(current + 1, q.right))



#         x = recursive_max_depth(0, root)

#         return x

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        max_depth = 0

        while queue:
            node, depth = queue.popleft()
            max_depth = depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return max_depth

