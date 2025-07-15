#!/usr/bin/env python3

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        i = len(columnTitle) - 1
        result = 0

        for char in columnTitle:
            index_value = ord(char) - 65
            current_value = (index_value + 1) * (26 ** i)
            result += current_value
            i -= 1

        return result



columnTitle = "A"
print(Solution().titleToNumber(columnTitle))

columnTitle = "B"
print(Solution().titleToNumber(columnTitle))

columnTitle = "C"
print(Solution().titleToNumber(columnTitle))

columnTitle = "Z"
print(Solution().titleToNumber(columnTitle))

columnTitle = "AA"
print(Solution().titleToNumber(columnTitle))

columnTitle = "AB"
print(Solution().titleToNumber(columnTitle))

columnTitle = "ZY"
print(Solution().titleToNumber(columnTitle))
