#!/usr/bin/env python3
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_string = min(strs, key=len)

        left = 0
        right = len(shortest_string)
        last_common_prefix = ""

        while left < right:
            mid = (left + right) // 2
            string_set: str = shortest_string[0 : mid + 1]
            check = True

            for element in strs:
                if not element.startswith(string_set):
                    check = False
                    break

            if check:
                left = mid + 1
                last_common_prefix = string_set
            else:
                right = mid

        return last_common_prefix


strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))

strs = ["dog","racecar","car"]
print(Solution().longestCommonPrefix(strs))

strs = ["cir","car"]
print(Solution().longestCommonPrefix(strs))

strs = ["flower","flower","flower","flower"]
print(Solution().longestCommonPrefix(strs))
