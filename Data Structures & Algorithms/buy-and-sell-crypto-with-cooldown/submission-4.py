class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        dp = [0] * n
        res = 0
        for l in range(n-2, -1, -1):
            for r in range(l+1, n):
                diff = prices[r] - prices[l]
                nxt = 0
                for i in range (r+2, n):
                    nxt = max(nxt, dp[i])
                dp[l] = max(dp[l], diff + nxt)

        return max(dp)
