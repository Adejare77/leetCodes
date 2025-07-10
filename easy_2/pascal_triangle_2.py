#!/usr/bin/env python3
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_list = [1]

        for i in range(rowIndex):
            current_list = [1]
            for j in range(1, len(prev_list)):
                current_list.append(prev_list[j - 1] + prev_list[j])
            current_list.append(1)
            prev_list = current_list

        return prev_list

rowIndex = 3
print(Solution().getRow(rowIndex))

rowIndex = 0
print(Solution().getRow(rowIndex))

rowIndex = 1
print(Solution().getRow(rowIndex))

rowIndex = 5
print(Solution().getRow(rowIndex))
