#!/usr/bin/env python3
import math

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        s = []

        # Iterate over the pairs of values and symbols
        for value, symbol in roman_numerals.items():
            quotient = num // value

            if quotient > 0:
                s.append(symbol * quotient)
                num %= value

        return "".join(s)


print(Solution().intToRoman(1))
print(Solution().intToRoman(4))
print(Solution().intToRoman(7))
print(Solution().intToRoman(9))
print(Solution().intToRoman(15))
print(Solution().intToRoman(1900))
print(Solution().intToRoman(1915))
print(Solution().intToRoman(19))
print(Solution().intToRoman(69))
print(Solution().intToRoman(30))
print(Solution().intToRoman(40))
print(Solution().intToRoman(50))
print(Solution().intToRoman(80))
print(Solution().intToRoman(90))
print(Solution().intToRoman(100))
print(Solution().intToRoman(400))
print(Solution().intToRoman(500))
print(Solution().intToRoman(900))
print(Solution().intToRoman(947))
print(Solution().intToRoman(1000))
