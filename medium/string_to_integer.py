#!/usr/bin/env python3

class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0

        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        sign = 1
        start = end = -1

        for idx, char in enumerate(s):
            if start == -1 and char == " ":
                pass

            elif start == -1 and (char == "-" or char == "+"):
                sign = 1 if char == "+" else -1
                start += 1

            elif char in digits:
                if end == -1:
                    start = idx
                end = idx + 1

            else:
                break

        try:
            if sign == 1:
                return int(s[start:end]) if int(s[start:end]) < (2**31 - 1) else (2**31 - 1)
            return sign * int(s[start:end]) if int(s[start:end]) < 2**31 else sign * 2**31
        except ValueError:
            return 0


s = "42"
print(Solution().myAtoi(s))

s = "-42"
print(Solution().myAtoi(s))

s = "1337c0d3"
print(Solution().myAtoi(s))

s = "0-1"
print(Solution().myAtoi(s))

s = "words and 987"
print(Solution().myAtoi(s))

s = ""
print(Solution().myAtoi(s))

s = f"{-2**32}"
print(Solution().myAtoi(s))

s = "+1"
print(Solution().myAtoi(s))

s = "-91283472332"
print(Solution().myAtoi(s))

s = "21474836460"
print(Solution().myAtoi(s))
