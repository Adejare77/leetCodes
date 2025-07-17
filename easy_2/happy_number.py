#!/usr/bin/env python3

class Solution:
    # def isHappy(self, n: int) -> bool:
    #     check = set()
    #     while True:
    #         if n in check:
    #             return False
    #         check.add(n)
    #         stringify_n = str(n)
    #         result = 0
    #         for i in stringify_n:
    #             result += int(i) ** 2
    #         if result == 1:
    #             return True
    #         n = result


    def isHappy(self, n: int) -> bool:
        check = set()
        while n:
            if n in check:
                return False
            check.add(n)

            result = 0
            while n > 0:
                result += (n % 10) ** 2
                n //= 10

            if result == 1:
                return True
            n = result

n = 19
print(Solution().isHappy(n))

n = 2
print(Solution().isHappy(n))
