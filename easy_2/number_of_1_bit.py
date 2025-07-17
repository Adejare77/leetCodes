#!/usr/bin/env python3

class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_bits = format(n, 'b')
        count = 0
        for bit in binary_bits:
            count = count + 1 if bit == '1' else count
        return count

n = 11
print(Solution().hammingWeight(n))

n = 128
print(Solution().hammingWeight(n))
