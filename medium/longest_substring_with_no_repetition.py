#!/usr/bin/env python3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 0
        char_index = {}

        for idx, char in enumerate(s):
            if char in char_index:
                start = max(start, char_index[char] + 1)

            char_index[char] = idx
            max_len = max(max_len, idx + 1 - start)

        return max_len

s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))

s = " "
print(Solution().lengthOfLongestSubstring(s))

s = "a"
print(Solution().lengthOfLongestSubstring(s))

s = "ab"
print(Solution().lengthOfLongestSubstring(s))

s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))
