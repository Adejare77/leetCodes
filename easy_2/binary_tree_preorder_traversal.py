#!/usr/bin/env python3
from typing import Optional, List
from my_bfs_expansion import toBinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []

        def preorderRecursion(root: Optional[TreeNode]) -> None:
            result.append(root.val)

            if not root.left and not root.right:
                return

            if root.left and not root.right:
                return preorderRecursion(root.left)

            if not root.left and root.right:
                return preorderRecursion(root.right)

            preorderRecursion(root.left)
            preorderRecursion(root.right)

            return

        preorderRecursion(root)
        return result


nums = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
root = toBinaryTree(nums)
print(Solution().preorderTraversal(root))

nums = [1, None, 2, 3]
root = toBinaryTree(nums)
print(Solution().preorderTraversal(root))

nums = []
root = toBinaryTree(nums)
print(Solution().preorderTraversal(root))

nums = [1]
root = toBinaryTree(nums)
print(Solution().preorderTraversal(root))
