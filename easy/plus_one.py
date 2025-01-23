#!/usr/bin/env python3
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 == 10:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits


digits = [1, 2, 3]
print(Solution().plusOne(digits))

digits = [4,3,2,1]
print(Solution().plusOne(digits))

digits = [9]
print(Solution().plusOne(digits))
