#!/usr/bin/env python3

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            indexPosition = columnNumber - 1
            remainder = indexPosition % 26

            result = chr(65 + remainder) + result
            columnNumber = indexPosition // 26

        return result


columnNumber = 1
print(Solution().convertToTitle(columnNumber))

columnNumber = 2
print(Solution().convertToTitle(columnNumber))

columnNumber = 3
print(Solution().convertToTitle(columnNumber))

columnNumber = 26
print(Solution().convertToTitle(columnNumber))

columnNumber = 27
print(Solution().convertToTitle(columnNumber))

columnNumber = 28
print(Solution().convertToTitle(columnNumber))

columnNumber = 701
print(Solution().convertToTitle(columnNumber))
