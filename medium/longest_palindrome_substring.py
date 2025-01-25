#!/usr/bin/env python3

class Solution:
    def longestPalindrome(self, s: str) -> int:
        def palindrome(left: int, right: int) -> int:
            if left < 0 or right >= len(s) or s[left] != s[right]:
                return 0
            return 2 + palindrome(left - 1, right + 1)

        max_len = 0
        for idx in range(len(s)):
            remainder = len(s) - 1 - idx
            # Early return if the current idx max_len cannot be greater than
            # already found one. 2 (for both left and right), 1 for the current idx
            if max_len >= remainder * 2 + 1:
                break
            even = palindrome(idx, idx + 1)
            odd = 1 + palindrome(idx - 1, idx + 1)

            max_len = max(max_len, even, odd)

        return max_len

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(left: int, right: int) -> int:
            if left < 0 or right >= len(s) or s[left] != s[right]:
                if right - left > len(longest): # To minimize slicing
                    return s[left + 1:right] # returns the last palindrome
                return ""

            return palindrome(left - 1, right + 1)

        longest = ""

        for idx in range(len(s)):
            # Early return if current idx and following idx max_len cannot be greater than already found one.
            remainder = len(s) - 1 - idx # number of idx left to check for
            if len(longest) >= remainder * 2 + 1: # *2 for left and right, 1 for current idx
                break

            even_palindrome = palindrome(idx, idx + 1)
            odd_palindrome = palindrome(idx, idx)

            longest = max(longest, even_palindrome, odd_palindrome, key=len)

        return longest


s = "babad"
print(Solution().longestPalindrome(s))

s = "bbbb"
print(Solution().longestPalindrome(s))

s = "cbbd"
print(Solution().longestPalindrome(s))

s = "a"
print(Solution().longestPalindrome(s))

s = "aaaacaaa"
print(Solution().longestPalindrome(s))

s = "abcdee"
print(Solution().longestPalindrome(s))
