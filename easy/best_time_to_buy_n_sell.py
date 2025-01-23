#!/usr/bin/env python3
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        left, right = 0, 1
        buy, sell = prices[left], prices[right]
        result = max(0, sell - buy)

        while right + 1 < len(prices):
            left += 1
            right += 1
            sell = prices[right]

            if prices[left] < buy:
                buy = prices[left]

            result = max(result, sell - buy)

        return result

prices = [7,1,5,3,6,4]  # 5
print(Solution().maxProfit(prices))
prices = [7,6,4,3,1]    # 0
print(Solution().maxProfit(prices))
prices = [1,4,2]    # 3
print(Solution().maxProfit(prices))
prices = [2, 7, 1, 3, 4, 5] # 5
print(Solution().maxProfit(prices))
prices = [2,1,2,1,0,1,2] # 2
print(Solution().maxProfit(prices))

