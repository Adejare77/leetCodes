#!/usr/bin/env python3
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        start = len(digits) - 1


        while start >= 0:
            if start == 0 and digits[start] == 9:
                digits[start] = 1
                digits.append(0)
                break

            if digits[start] != 9:
                digits[start] += + 1
                break

            digits[start] = 0

            start -= 1

        return digits


digits = [1, 2, 3]
Solution().plusOne(digits)
print(digits)

digits = [8, 9]
Solution().plusOne(digits)
print(digits)

digits = [9, 9, 9]
Solution().plusOne(digits)
print(digits)

digits = [4, 3, 2, 1]
Solution().plusOne(digits)
print(digits)

digits = [9]
Solution().plusOne(digits)
print(digits)

digits = [2, 9, 9]
Solution().plusOne(digits)
print(digits)

digits = [2, 8, 8, 9, 9]
Solution().plusOne(digits)
print(digits)

digits = [8,9,9,9] # [9, 0, 0, 0]
Solution().plusOne(digits)
print(digits)

digits = [2, 3,3,3,3,4,4,4,4,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9, 9, 9]
Solution().plusOne(digits)
print(digits)
