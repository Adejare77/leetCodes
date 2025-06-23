#!/usr/bin/env python3

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pt1 = list1
        pt2 = list2

        head = tmp = ListNode()
        while pt1 or pt2:
            if pt1 and pt2:
                if pt1.val <= pt2.val:
                    tmp.next = pt1
                    tmp = tmp.next
                    pt1 = pt1.next
                else:
                    tmp.next = pt2
                    tmp = tmp.next
                    pt2 = pt2.next
            elif pt1:
                tmp.next = pt1
                break
            else:
                tmp.next = pt2
                break

        return head.next
