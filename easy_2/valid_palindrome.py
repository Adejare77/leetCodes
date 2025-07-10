#!/usr/bin/env python3

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

# s = "A man, a plan, a canal: Panama"
# print(Solution().isPalindrome(s))

s = "0P"
print(Solution().isPalindrome(s))

# s = "race a car"
# print(Solution().isPalindrome(s))

# s = " "
# print(Solution().isPalindrome(s))
