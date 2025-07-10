#!/usr/bin/env python3
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m + n - 1
        m_index = m - 1
        n_index = n - 1

        while i >= 0:
            if m_index < 0:
                nums1[: i+1] = nums2[: n_index+1]
                break
            elif n_index < 0:
                nums1[: i+1] = nums1[: m_index+1]
                break
            elif nums1[m_index] >= nums2[n_index]:
                nums1[i] = nums1[m_index]
                m_index -= 1
            else:
                nums1[i] = nums2[n_index]
                n_index -= 1

            i -= 1

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

Solution().merge(nums1, 3, nums2, 3)
print(nums1)

nums1 = [1]
nums2 = []

Solution().merge(nums1, 1, nums2, 0)
print(nums1)

nums1 = []
nums2 = [1]

Solution().merge(nums1, 0, nums2, 1)
print(nums1)
