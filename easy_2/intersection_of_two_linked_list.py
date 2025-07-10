#!/usr/bin/env python3

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        switchA = switchB = True
        ptr1 = headA
        ptr2 = headB

        while ptr1 or ptr2:
            if ptr1 == ptr2:
                return ptr1

            ptr1 = ptr1.next
            ptr2 = ptr2.next

            if not ptr1 and switchA:
                switchA = False
                ptr1 = headB

            if not ptr2 and switchB:
                switchB = False
                ptr2 = headA
