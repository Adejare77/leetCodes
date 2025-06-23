#!/usr/bin/env python3

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_format = str(x)
        left = 0
        right = len(string_format) - 1
        while left < right:
            if string_format[left] != string_format[right]:
                return False
            left += 1
            right -= 1

        return True

x = 121
print(Solution().isPalindrome(x))

x = -121
print(Solution().isPalindrome(x))

x = 10
print(Solution().isPalindrome(x))
