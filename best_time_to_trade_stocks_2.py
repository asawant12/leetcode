# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for index in range(len(prices)-1):
            min_price = prices[index]
            curr_price = prices[index + 1]
            if curr_price < min_price:
                min_price = curr_price
            else:
                profit = profit + (curr_price - min_price)
        
        print(profit) 
        return profit
