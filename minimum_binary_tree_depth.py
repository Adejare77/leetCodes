#!/usr/bin/env python3
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Using Recursion
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return 1 + min(left, right) if left and right else 1 + max(left, right)

# Using Iteration
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        pass
