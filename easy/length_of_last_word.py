#!/usr/bin/env python3


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        last_word = s.split()[-1]

        return len(last_word)


s = "Hello world"
print(Solution().lengthOfLastWord(s))
s = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s))
s = "luffy is still joyboy"
print(Solution().lengthOfLastWord(s))
