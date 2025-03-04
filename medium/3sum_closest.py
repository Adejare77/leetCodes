#!/usr/bin/env python3
from typing import List

# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         nearest_sum = nums[-1] + nums[-2] + nums[-3]

#         for i in range(len(nums) - 3):
#             if (nums[i] - target) >= abs(nearest_sum - target):
#                 break
#             if i > 0 and nums[i-1] == nums[i]:
#                 continue

#             # print("**********", i)
#             left, right = i + 1, len(nums) - 1
#             while left < right:
#                 if nums[i] + nums[left] - target > abs(nearest_sum - target):
#                     break
#                 if left - 1 != i and nums[left - 1] == nums[left]:
#                     left += 1
#                     continue
#                 if right < len(nums) - 1 and nums[right] == nums[right + 1]:
#                     right -= 1
#                     continue

#                 total_sub_sum = nums[i] + nums[left] + nums[right]

#                 if abs(total_sub_sum - target) <= abs(nearest_sum - target):
#                     nearest_sum = total_sub_sum
#                     if abs(nearest_sum) == abs(target):
#                         return nearest_sum
#                     elif abs(nearest_sum) < abs(target):
#                         left += 1
#                     else:
#                         right -= 1
#                 else:
#                     right -= 1

#         return nearest_sum

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        nearest_sum = nums[-1] + nums[-2] + nums[-3]

        for i in range(len(nums) - 3):
            if target > 0 and (nums[i] - target) >= abs(nearest_sum - target):
                break

            if i > 0 and nums[i-1] == nums[i]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                if target > 0 and  nums[i] + nums[left] - target > abs(nearest_sum - target):
                    break
                elif left - 1 != i and nums[left - 1] == nums[left]:
                    left += 1
                elif right < len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                else:
                    total_sub_sum = nums[i] + nums[left] + nums[right]

                    if abs(total_sub_sum - target) <= abs(nearest_sum - target):
                        nearest_sum = total_sub_sum
                        if nearest_sum == target:
                            return nearest_sum
                        elif nearest_sum < target:
                            left += 1
                        else:
                            right -= 1
                    else:
                        right -= 1

        return nearest_sum


# nums = [-1,2,1,-4]  # 2
# target = 1
# print(Solution().threeSumClosest(nums, target))

# nums = [0, 0, 0] # 0
# target = 1
# print(Solution().threeSumClosest(nums, target))

# nums = [-2, 2, 4, 3, 0, -9, 2, 5] # Expected 8
# target = 8
# print(Solution().threeSumClosest(nums, target))

# nums = [10,20,30,40,50,60,70,80,90]  # Expected 60
# target = 1
# print(Solution().threeSumClosest(nums, target))

# nums = [-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1]  # Expected -15
# target = -14
# print(Solution().threeSumClosest(nums, target))

nums = [-84,92,26,19,-7,9,42,-51,8,30,-100,-13,-38]  # Expected 77
target = 78
print(Solution().threeSumClosest(nums, target))

print("************")
print(nums)
print("************")
