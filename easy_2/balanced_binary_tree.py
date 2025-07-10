#!/usr/bin/env python3
from typing import Optional
from my_bfs_expansion import toBinaryTree, bfs

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True

#         lowest_highest = set()
#         def checkIsBalanced(level: int, root: Optional[TreeNode]):
#             if not root:
#                 print(root, level)
#                 lowest_highest.add(level)
#                 return

#             if lowest_highest and max(lowest_highest) - min(lowest_highest) not in [-1, 0, 1]:
#                 return

#             checkIsBalanced(level + 1, root.left)
#             checkIsBalanced(level + 1, root.right)

#         checkIsBalanced(0, root)

#         diff = max(lowest_highest) - min(lowest_highest)
#         if lowest_highest and diff not in [-1, 0, 1]:
#             print(lowest_highest)
#             return False

#         return True

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def checkHeight(root: TreeNode) -> bool:
            if not root:
                return 0

            left = checkHeight(root.left)
            if left == -1:
                return -1

            right = checkHeight(root.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return checkHeight(root) != -1

nums = [3,9,20,None,None,15,7]  # True
root = toBinaryTree(nums)
print(Solution().isBalanced(root))

nums =[1,2,2,3,3,None,None,4,4]  # False
root = toBinaryTree(nums)
print(Solution().isBalanced(root))

nums =[]  # True
root = toBinaryTree(nums)
print(Solution().isBalanced(root))

nums =[1,2]  # True
root = toBinaryTree(nums)
print(Solution().isBalanced(root))

nums = [1,2,3,4,5,6,None,8]  # True
root = toBinaryTree(nums)
print(Solution().isBalanced(root))
