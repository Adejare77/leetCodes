#!/usr/bin/env python3
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode(0)
        tmp = new_node
        rem = 0

        while l1 or l2:
            if l1 and l2:
                value = (rem + l1.val + l2.val) % 10
                rem = (rem + l1.val + l2.val) // 10
                l1, l2 = l1.next, l2.next

            elif l1:
                value = (rem + l1.val) % 10
                rem = (rem + l1.val) // 10
                l1 = l1.next

            else:
                value = (rem + l2.val) % 10
                rem = (rem + l2.val) // 10
                l2 = l2.next

            tmp.next = ListNode(value)
            tmp = tmp.next

        if rem:
            tmp.next = ListNode(rem)

        return new_node.next

