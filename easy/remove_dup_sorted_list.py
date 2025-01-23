#!/usr/bin/env python3

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = head
        current = prev.next

        while current:
            if current.val == prev.val:
                current = current.next
                prev.next = current
                continue

            prev = current
            current = current.next

        return head
