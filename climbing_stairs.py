#!/usr/bin/env python3

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0:
#             return 1
#         elif n == 1:
#             return 1

#         return self.climbStairs(n-1) + self.climbStairs(n-2)

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base Case
        if n <= 1:
            return 1

        i = 2
        last_prev = 1
        last_two_prev = 1

        while i <= n:
            current_sum = last_prev + last_two_prev
            last_two_prev, last_prev = last_prev, current_sum
            i += 1

        return current_sum


n = 2
print(Solution().climbStairs(n))
n = 3
print(Solution().climbStairs(n))
n = 1
print(Solution().climbStairs(n))
n = 5
print(Solution().climbStairs(n))
n = 7
print(Solution().climbStairs(n))
n = 6
print(Solution().climbStairs(n))
n = 44
print(Solution().climbStairs(n))
