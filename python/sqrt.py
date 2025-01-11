#!/usr/bin/env python3

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        low = 0
        high = x
        result = 0

        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                result = mid
                low = mid + 1


        return result

print(Solution().mySqrt(8))
print(Solution().mySqrt(3))
print(Solution().mySqrt(4))
print(Solution().mySqrt(2))
print(Solution().mySqrt(6))
print(Solution().mySqrt(5))

