#!/usr/bin/env python3

class Solution:
    def reverse(self, x: int) -> int:
        largest_value = 2**31 - 1

        result = 0
        sign = 1 if x >= 0 else -1

        x = abs(x)
        while x:
            rem = x % 10
            x = x // 10

            result = result * 10 + rem
            if result >= largest_value:
                return 0


        return result * sign

print(Solution().reverse(123))
print(Solution().reverse(-321))
print(Solution().reverse(120))
