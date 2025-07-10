#!/usr/bin/env python3
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        result = [[1], [1, 1]]

        for i in range(2, numRows):
            tmp = [1]
            prev = result[i - 1]
            for j in range(1, len(prev)):
                tmp.append(prev[j - 1] + prev[j])
            tmp.append(1)
            result.append(tmp)

        return result

numRows = 5
print(Solution().generate(numRows))
