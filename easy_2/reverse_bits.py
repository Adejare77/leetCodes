#!/usr/bin/env python3

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        i = 32

        while i:
            i -= 1
            last_bit = n & 1  # selects last bit in n
            result <<=  1  # left shift to accomodate more bits
            result = result | last_bit  # adds last bit to result
            n >>= 1  # right shift to have new last bit

        return result


n = int("00000010100101000001111010011100", base=2)
print(Solution().reverseBits(n))
