#!/usr/bin/env python3
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Use three pointers. one static, two dynamic
        sorted_list = sorted(nums)
        last_list = []
        result = []

        for i in range(len(sorted_list) - 2):
            left = i+1
            right = len(sorted_list) - 1

            if sorted_list[i] > 0:
                break

            if i > 0 and sorted_list[i] == sorted_list[i-1]:
                continue

            while left < right:
                current_list = [sorted_list[i], sorted_list[left], sorted_list[right]]
                total_sum = sum(current_list)

                if (left > i + 1) and sorted_list[left] == sorted_list[left-1]:
                    left += 1
                    continue

                if sum([sorted_list[i], sorted_list[left]]) > 0:
                    break

                elif total_sum == 0 and current_list != last_list:
                    last_list = current_list
                    result.append(current_list)
                    left += 1
                    right -= 1

                elif total_sum > 0:
                    right -= 1

                else:
                    left += 1

        return result

# nums = [-1, 0, 1, 2, -1, -4]
# print(Solution().threeSum(nums))

# nums = [0, 1, 1]
# print(Solution().threeSum(nums))

# nums = [0, 0, 0]
# print(Solution().threeSum(nums))

# nums = [0, 0, 0, -1, -1, -1, -1, 4, -4]
# print(Solution().threeSum(nums))

nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
print(Solution().threeSum(nums))
