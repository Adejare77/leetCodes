#!/usr/bin/env python
from typing import List


# class Solution:
#     def subarrays(self, arr: List[int]) -> List[List[int]]:
#         result = []
#         start = 0

#         for ele in arr:
#             end = len(result) + 1
#             for index in range(start, end):
#                 if index == end - 1:
#                     result.append([ele])
#                 else:
#                     result.append(result[index].copy() + [ele])

#             start = index

#         return result


class Solution:
    def subarrays(self, arr: List[int]) -> List[List[int]]:
        result = []
        n = len(arr)

        # Generate subarrays using nested loops
        for start in range(n):
            current_subarray = []
            for end in range(start, n):
                current_subarray.append(arr[end])  # Extend subarray
                result.append(current_subarray.copy())  # Add to result

        return result


arr = ['a', 'b', 'c', 'd', 'e']

print(Solution().subarrays(arr))
