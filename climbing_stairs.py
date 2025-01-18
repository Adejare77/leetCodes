#!/usr/bin/env python3

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 1

        return self.climbStairs(n-1) + self.climbStairs(n-2)



n = 2
print(Solution().climbStairs(n))
n = 3
print(Solution().climbStairs(n))
# n = 1
# print(Solution().climbStairs(n))
# n = 5
# print(Solution().climbStairs(n))
# n = 7
# print(Solution().climbStairs(n))
n = 6
print(Solution().climbStairs(n))
