#!/usr/bin/env python3
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        left = 0
        sub_sum = nums[left]

        for right in range(1, n):
            sub_sum += nums[right]
            if sub_sum % k == 0:
                return True
            sub_sum_copy = sub_sum
            while (left + 1 < right):
                sub_sum_copy -= nums[left]
                if sub_sum_copy % k == 0:
                    return True
                left += 1
            left = 0
        return False

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False

        # Dictionary to store remainders
        remainder_map = {0: -1}  # Initialize with 0 remainder at index -1
        sub_sum = 0

        for i in range(n):
            sub_sum += nums[i]
            remainder = sub_sum % k

            if remainder in remainder_map:
                # Check if subarray length is at least 2
                print(remainder_map)
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i  # Store the first occurrence of this remainder

        return False


# nums = [23, 2, 4, 6, 7]
# k = 6
# print(Solution().checkSubarraySum(nums, k))
# nums = [23,2,6,4,7]
# k = 6
# print(Solution().checkSubarraySum(nums, k))
# nums = [23, 2, 6, 4, 7]
# k = 13
# print(Solution().checkSubarraySum(nums, k))

nums = [7, 6, 5]
k = 6
print(Solution().checkSubarraySum(nums, k))
