#!/usr/bin/env python3

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total_sum = int(a, 2) + int(b, 2)
        return format(total_sum, 'b')

a = '11'
b = '1'

print(Solution().addBinary(a, b))

a = '1010'
b = '1011'

print(Solution().addBinary(a, b))
