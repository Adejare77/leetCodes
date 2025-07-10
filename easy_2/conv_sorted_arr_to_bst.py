#!/usr/bin/env python3
from typing import List, Optional
from my_bfs_expansion import bfs
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         def bst(low: int, high: int) -> Optional[TreeNode]:
#             if low >= high:
#                 return None

#             mid = (low + high) // 2
#             node = TreeNode(nums[mid])

#             node.left = bst(low, mid)
#             node.right = bst(mid + 1, high)

#             return node

#         return bst(0, len(nums))


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums) // 2
        # [TreeNode, low, mid, high]
        head = TreeNode(nums[mid])
        queue = deque([(head, 0, mid, len(nums))])
        i = 1

        while i < len(nums):
            # For left
            node, low, mid, high = queue.popleft()
            m = (low + mid) // 2
            if m >= 0 and m < mid:
                newNode = TreeNode(nums[m])
                node.left = newNode
                queue.append((newNode, low, m, mid))
                i += 1

            # For right
            m = ((mid + 1) + high) // 2
            if m < high:
                newNode = TreeNode(nums[m])
                node.right = newNode
                queue.append((newNode, mid+1, m, high))
                i += 1

        return head



nums = [-10,-3]
root = Solution().sortedArrayToBST(nums)
result = bfs(root)
print(result)


nums = [-10,-3,0,5,9]
root = Solution().sortedArrayToBST(nums)
result = bfs(root)
print(result)


nums = [0,1,2,3,4,5,6,7,8]  # [4,2,7,1,3,6,8,0,null]
root = Solution().sortedArrayToBST(nums)
result = bfs(root)
print(result)
