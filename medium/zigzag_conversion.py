#!/usr/bin/env python3
from typing import List, Tuple


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        array = []
        i = 0
        switch = False
        for char in s:
            try:
                array[i].append(char)
            except IndexError:
                array.append([char])

            if i-1 < 0 or i+1 == numRows:
                switch = not switch
            i = i+1 if switch else i-1

        result = [''.join(row) for row in array]
        return "".join(result)



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = []
        switch = True
        i = track = 0

        def jump_algo(row: int, switch: bool) -> Tuple[int, bool]:
            if row == 0:
                switch = True
            elif row == numRows - 1:
                switch = False

            if numRows == 1:
                result = 1
            else:
                result = ((numRows - 1) - row) * 2 if switch else row * 2

            return result, not switch

        for _ in range(len(s)):
            if i >= len(s):
                switch = True
                track += 1
                i = track

            result.append(s[i])
            jump, switch = jump_algo(track, switch)

            i += jump


        return "".join(result)



s = "PAYPALISHIRING"  # PAHNAPLSIIGYIR
numRows = 3
print(Solution().convert(s, numRows))

s = "PAYPALISHIRING"  # "PINALSIGYAHRPI"
numRows = 4
print(Solution().convert(s, numRows))

s = "A"
numRows = 1
print(Solution().convert(s, numRows))

s = "AB"
numRows = 1
print(Solution().convert(s, numRows))

s = "ABC"
numRows = 2
print(Solution().convert(s, numRows))
