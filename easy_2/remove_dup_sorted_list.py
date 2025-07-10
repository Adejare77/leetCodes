#!/usr/bin/env python3
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        tmp: ListNode = head
        current: ListNode = tmp.next
        values = {tmp.val}

        while current:
            if current.val in values:
                current = current.next
                tmp.next = current

            else:
                values.add(current.val)
                current = current.next
                tmp = tmp.next

        return head
