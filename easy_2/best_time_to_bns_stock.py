#!/usr/bin/env python3
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        left = 0
        right = 1
        profit = 0

        while right < len(prices):
            diff = prices[right] - prices[left]
            if diff > 0:
                profit = max(profit, diff)
            else:
                left = right

            right += 1

        return profit


    # def maxProfit(self, prices: List[int]) -> int:
    #     left = 0
    #     right = len(prices) - 1
    #     selling_price = prices[right]
    #     buying_price = prices[left]
    #     profit = 0

    #     while left <= right:
    #         if prices[right] > selling_price:
    #             selling_price = prices[right]
    #         else:
    #             profit = max(profit, selling_price - prices[right])

    #         if prices[left] < buying_price:
    #             buying_price = prices[left]
    #         else:
    #             profit = max(profit, prices[left] - buying_price)


    #         profit = max(profit, selling_price - buying_price)

    #         right -= 1
    #         left += 1

    #     return profit


prices = [1]
print(Solution().maxProfit(prices))

prices = [3,1,6,5,8,3]
print(Solution().maxProfit(prices))

prices = [3,2,6,5,0,3]
print(Solution().maxProfit(prices))

prices = [3,2,6,5,0,5]
print(Solution().maxProfit(prices))

prices = [1,4,2]
print(Solution().maxProfit(prices))

prices = [2,1,4]
print(Solution().maxProfit(prices))

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))

prices = [7]
print(Solution().maxProfit(prices))

prices = [7, 2]
print(Solution().maxProfit(prices))

prices = [1,1,5,3,6,8]
print(Solution().maxProfit(prices))

prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
