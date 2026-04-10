class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        cur_min = float('inf')
        n = len(prices)
        # dp[i] maximum profit for i days
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            price = prices[i - 1]
            cur_min = min(cur_min, price)
            dp[i] = max(dp[i - 1], price - cur_min)
        return dp[n]