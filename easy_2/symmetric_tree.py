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
        if not root:
            return True

        def checkSymmetric(p: Optional[TreeNode], q: Optional[TreeNode]):
            if not p and not q:
                return True
            if not p and q:
                return False
            if not q and p:
                return False

            if q.val != p.val:
                return False

            return checkSymmetric(p.left, q.right) and checkSymmetric(p.right, q.left)

        return checkSymmetric(root.left, root.right)
