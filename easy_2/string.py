#!/usr/bin/env python3


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = haystack.find(needle)
        return result



haystack = "sadbutsad"
needle = "sad"

print(Solution().strStr(haystack, needle))


# haystack = "leetcode"
# needle = "leeto"
# print(Solution().strStr(haystack, needle))
