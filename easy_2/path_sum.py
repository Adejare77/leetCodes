#!/usr/bin/env python3
from typing import Optional
from my_bfs_expansion import toBinaryTree
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False

#         def checkSum(current_sum: int, node: Optional[TreeNode]) -> bool:
#             current_sum += node.val

#             if not node.left and not node.right:
#                 return current_sum == targetSum

#             if node.left and checkSum(current_sum, node.left):
#                 return True

#             if node.right and checkSum(current_sum, node.right):
#                 return True

#             return False

#         return checkSum(0, root)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue = deque([(root, 0)]) # (node, current_sum)

        while queue:
            node, current_sum = queue.popleft()
            current_sum += node.val

            if not node.left and not node.right and current_sum == targetSum:
                return True

            if node.left:
                queue.append((node.left, current_sum))

            if node.right:
                queue.append((node.right, current_sum))

        return False


nums = [1, 2, 5]
targetSum = 5
root = toBinaryTree(nums)

print(Solution().hasPathSum(root, targetSum))
