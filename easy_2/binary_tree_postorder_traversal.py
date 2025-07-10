#!/usr/bin/env python3
from typing import List, Optional
from my_bfs_expansion import toBinaryTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        def postorder_recursion(root: Optional[TreeNode]) -> None:
            if not root.left and not root.right:
                result.append(root.val)
                return

            if root.left:
                postorder_recursion(root.left)

            if root.right:
                postorder_recursion(root.right)

            result.append(root.val)

        postorder_recursion(root)
        return result

nums = [1,2,3,4,5,None,8,None,None,6,7,9]
root = toBinaryTree(nums)
print(Solution().postorderTraversal(root))

nums = []
root = toBinaryTree(nums)
print(Solution().postorderTraversal(root))
