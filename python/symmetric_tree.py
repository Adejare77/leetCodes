#!/usr/bin/env python3
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetry(p: Optional[TreeNode], q: Optional[TreeNode]):
            if not p and not q:
                return True
            if (not p and q) or (not q and p):
                return False

            return (
                p.val == q.val and symmetry(p.left, q.right) and symmetry(p.right, q.left)
            )

        return symmetry(root.left, root.right)
