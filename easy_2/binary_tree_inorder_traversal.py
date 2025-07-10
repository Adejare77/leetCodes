#!/usr/bin/env python3
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Inorder Traversal = left->root->right
        output = []
        if not root:
            return output

        def recursive_inorder(root: Optional[TreeNode]):
            if not root:
                return
            if root.left:
                recursive_inorder(root.left)

            output.append(root.val)

            if root.right:
                recursive_inorder(root.right)

        recursive_inorder(root)

        return output
