#!/usr/bin/env python
from typing import List


# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         if n == 0:
#             return None

#         elif m == 0:
#             nums1[:] = nums2
#             return None

#         j = k = 0
#         ptr1, ptr2 = nums1[j], nums2[k]
#         highest_value = nums1[m-1] if nums1[m-1] >= nums2[n-1] else nums2[n-1]
#         track = [nums1[0]]

#         for i in range(m+n):
#             try:
#                 track.append(nums1[i+1])
#             except Exception:
#                 pass
#             if ptr1 <= ptr2:
#                 nums1[i] = ptr1
#                 j += 1
#                 ptr1 = track[j] if j < m else highest_value
#                 continue

#             nums1[i] = ptr2
#             k += 1
#             ptr2 = highest_value if k >= n else nums2[k]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m == 0:
            nums1[:] = nums2
            return
        elif n == 0:
            return
        j, k = m - 1, n - 1
        ptr1 = nums1[j]
        ptr2 = nums2[k]

        for i in range(m+n - 1, -1, -1):
            if ptr1 >= ptr2:
                nums1[i] = ptr1
                j -= 1
                ptr1 = nums1[j] if j >= 0 else nums2[0]
                continue

            nums1[i] = ptr2
            k -= 1
            ptr2 = nums2[k] if k >= 0 else nums1[0]


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
Solution().merge(nums1, 3, nums2, 3)
print(nums1)

nums1 = [4, 5, 6, 0, 0, 0]
nums2 = [1, 2, 3]
Solution().merge(nums1, 3, nums2, 3)
print(nums1)

nums1 = [4, 5, 6, 0, 0, 0]
nums2 = [1, 3, 7]
Solution().merge(nums1, 3, nums2, 3)
print(nums1)

nums1 = [0]
nums2 = [1]

Solution().merge(nums1, 0, nums2, 1)
print(nums1)
nums1 = [4, 5, 6, 0, 0]
nums2 = [1, 7]
Solution().merge(nums1, 3, nums2, 2)
print(nums1)
