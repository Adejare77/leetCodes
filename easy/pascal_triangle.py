#!/usr/bin/env python3
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(1, numRows):
            current = [1]
            prev_list = result[-1]
            left, right = 0, 1
            while right < len(prev_list):
                current.append(prev_list[left] + prev_list[right])
                left += 1
                right += 1

            current.append(1)
            result.append(current)

        return result

print(Solution().generate(5))
