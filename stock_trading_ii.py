# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_ptr = 0
        while buy_ptr < len(prices)-1:
            buying_price = prices[buy_ptr]
            selling_price = prices[buy_ptr+1]
            if buying_price < selling_price:
                profit = profit + (selling_price - buying_price)
            buy_ptr += 1
        return profit
