#!/usr/bin/env python3

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        mid = 0

        while left < right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid
            else:
                left = mid + 1

        return mid if mid == left else mid + 1


# nums = [1, 3, 5, 6]
# target = 5

# print(Solution().searchInsert(nums, target))

# nums = [1, 3, 5, 6]
# target = 2

# print(Solution().searchInsert(nums, target))

nums = [1, 3, 5, 6]
target = 7

print(Solution().searchInsert(nums, target))

nums = [1,3,5,6]
target = 0

print(Solution().searchInsert(nums, target))

nums = [1,3,5]
target = 4

print(Solution().searchInsert(nums, target))
