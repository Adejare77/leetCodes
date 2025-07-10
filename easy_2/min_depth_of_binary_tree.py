#!/usr/bin/env python3

from typing import Optional
from collections import deque
from my_bfs_expansion import toBinaryTree, bfs

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         if not root.left and not root.right:
#             return 1

#         if not root.left:
#             return 1 + self.minDepth(root.right)

#         if not root.right:
#             return 1 + self.minDepth(root.left)

#         return min(1 + self.minDepth(root.left), 1 + self.minDepth(root.right))

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])  # (TreeNode, depth)

        while queue:
            node, depth = queue.popleft()

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))

            if not node.left and not node.right:
                return depth




nums = [3,9,20,None,None,15,7]
root = toBinaryTree(nums)
print(Solution().minDepth(root))

nums = [2,None,3,None,4,None,5,None,6]
root = toBinaryTree(nums)
result = bfs(root)
print(Solution().minDepth(root))
print(result)
