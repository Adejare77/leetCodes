#!/usr/bin/env python3

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         elif n == 2:
#             return 2

#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        prev_prev_val = 1
        prev_val = 1
        i = 2
        result = 0

        while i <= n:
            result = prev_prev_val + prev_val
            prev_val, prev_prev_val = result, prev_val

            i += 1

        return result



n = 1
print(Solution().climbStairs(n))

n = 2
print(Solution().climbStairs(n))

n = 3
print(Solution().climbStairs(n))

n = 4
print(Solution().climbStairs(n))

n = 5
print(Solution().climbStairs(n))

n = 6
print(Solution().climbStairs(n))

n = 7
print(Solution().climbStairs(n))

n = 44
print(Solution().climbStairs(n))
