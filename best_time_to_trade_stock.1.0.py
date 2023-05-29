# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        buy_ptr = 0
        sell_ptr = 1

        while sell_ptr < len(prices):
            buy_price = prices[buy_ptr]
            sell_price = prices[sell_ptr]
            if sell_price > buy_price:
                profit = sell_price - buy_price
                maxprofit = max(profit, maxprofit)
            else:
                buy_ptr = sell_ptr
            sell_ptr += 1
        return maxprofit
