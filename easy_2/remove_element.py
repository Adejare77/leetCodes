#!/usr/bin/env python3
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = -1
        count = 0

        for idx, num in enumerate(nums):
            if num == val:
                k = idx if k == -1 else k
                continue

            if k >= 0:
                nums[k], nums[idx] = nums[idx], nums[k]
                k += 1

            count += 1

        return count

nums = [0,1,2,2,3,0,4,2]
val = 2
print(Solution().removeElement(nums, val))
print(nums)

nums = [3, 2, 2, 3]
val = 3
print(Solution().removeElement(nums, val))
print(nums)
