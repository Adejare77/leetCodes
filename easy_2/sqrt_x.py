#!/usr/bin/env python3

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        if x == 1:
            return 1

        while left <= right:
            mid = (left + right) // 2

            if mid == left:
                return mid

            result = mid * mid
            if result == x:
                return mid

            if result > x:
                right = mid
            else:
                left = mid

        return left


x = 3
print(Solution().mySqrt(x))

x = 1
print(Solution().mySqrt(x))

x = 8
print(Solution().mySqrt(x))

x = 100
print(Solution().mySqrt(x))

x = 110
print(Solution().mySqrt(x))
