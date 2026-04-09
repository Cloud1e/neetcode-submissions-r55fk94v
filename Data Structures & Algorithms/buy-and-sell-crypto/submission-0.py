class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        cur_min = 10000
        n = len(prices)
        max_profit = 0
        for price in prices:
            cur_min = min(cur_min, price)
            max_profit = max(price - cur_min, max_profit)
        return max_profit