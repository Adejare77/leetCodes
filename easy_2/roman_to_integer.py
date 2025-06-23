#!/usr/bin/env python3

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        prev = roman_to_integer[s[0]]
        current_total = prev

        for i in range(1, len(s)):
            current_value = roman_to_integer[s[i]]
            if current_value > prev:
                current_total = current_total - prev + current_value - prev
            else:
                current_total += current_value

            prev = current_value

        return current_total


s = "III"
print(Solution().romanToInt(s))

s = "LVIII"
print(Solution().romanToInt(s))

s = "MCMXCIV"
print(Solution().romanToInt(s))
