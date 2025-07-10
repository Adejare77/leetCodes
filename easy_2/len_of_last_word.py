#!/usr/bin/env python3

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        start = -1

        s = s.rstrip()

        while count < len(s) and s[start] != " ":
            count += 1
            start -= 1

        return count


s = "Hello World"
print(Solution().lengthOfLastWord(s))

s = "   fly me to the moon"
print(Solution().lengthOfLastWord(s))

s = "luffy is still joyboy"
print(Solution().lengthOfLastWord(s))

s = "sample"
print(Solution().lengthOfLastWord(s))
