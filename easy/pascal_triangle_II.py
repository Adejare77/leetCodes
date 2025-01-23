#!/usr/bin/env python3
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]

        for i in range(rowIndex):
            current = [1]
            left, right = 0, 1

            while right < len(result):
                current.append(result[left] + result[right])
                left += 1
                right += 1

            current.append(1)
            result = current

        return result

print(Solution().getRow(3))
