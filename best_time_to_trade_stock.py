Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0]
        stock_price = prices
        while len(stock_price) > 1:
            max_price = max(stock_price)
            index = stock_price.index(max_price)
            min_price = max_price if not index else min(stock_price[:index])
            prof = max_price - min_price
            profit.append(prof)
            stock_price = stock_price[index+1:]
        
        print(max(profit)) 
        return max(profit)
