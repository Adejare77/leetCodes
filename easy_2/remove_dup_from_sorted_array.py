#!/usr/bin/env python3

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = set()
        last_idx = 0
        for i, num in enumerate(nums):
            if not num in unique_nums:
                unique_nums.add(num)
                if last_idx:
                    nums[i], nums[last_idx] = nums[last_idx], nums[i]
                    last_idx += 1
            else:
                if last_idx == 0:
                    last_idx = i

        return len(unique_nums)

nums = [1, 1, 2]
print(Solution().removeDuplicates(nums))

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))
