#!/usr/bin/env python3
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0
        for num in nums:
            unique ^= num

        return unique


nums = [2, 2, 1]
print(Solution().singleNumber(nums))

nums = [4, 1, 2, 1, 2]
print(Solution().singleNumber(nums))
