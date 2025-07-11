#!/usr/bin/env python3
from typing import List


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         group = {}
#         for i in nums:
#             if group.get(i):
#                 group[i] += 1
#                 if group[i] > len(nums) / 2:
#                     break
#             else:
#                 group[i] = 1

#         return max(group, key=group.get)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


nums = [1, 1, 2, 2, 3, 3, 3, 3]
print(Solution().majorityElement(nums))

nums = [3, 2, 2, 3, 3]
print(Solution().majorityElement(nums))

nums = [2, 2, 1, 1, 1, 2, 2]
print(Solution().majorityElement(nums))

nums = [2, 2, 1, 1, 1, 2, 2]
print(Solution().majorityElement(nums))
