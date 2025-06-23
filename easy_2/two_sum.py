#!/usr/bin/env python3
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}

        for index, element in enumerate(nums):
            diff = target - element
            if not element in rem:
                rem.update({diff: index})
            else:
                return [rem[element], index]


nums = [2, 7, 11, 15]
target = 9

print(Solution().twoSum(nums, target))
