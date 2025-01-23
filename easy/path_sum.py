#!/usr/bin/env python3
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def sumPath(root: Optional[TreeNode], current_sum: int):
            if not root:
                return False
            current_sum += root.val
            if not root.left and not root.right:
                return current_sum == targetSum

            return sumPath(root.left, current_sum) or sumPath(root.right, current_sum)

        return sumPath(root, 0)



from collections import deque

def level_order(root_level):
    if not root_level:
        return None

    array_len = len(root_level)
    root = TreeNode(root_level[0])
    queue = deque([root])
    i = 1

    while queue and i < len(root_level):
        node = queue.popleft()

        if i < array_len and root_level[i]:
            node.left = TreeNode(root_level[i])
            queue.append(node.left)
        i += 1
        if i < array_len and root_level[i]:
            node.right = TreeNode(root_level[i])
            queue.append(node.right)
        i += 1

    return root

root_array = [5,4,8,11,None,13,4,7,2,None,None,None,1]

root = level_order(root_array)


def level_order_print(root: Optional[TreeNode]):
    if not root:
        return

    queue = deque([root])
    while(queue):
        node = queue.popleft()
        if node:
            print(node.val)
            queue.append(node.left)
            queue.append(node.right)

# level_order_print(root)
print(Solution().hasPathSum(root, 22))
