class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        L = 0
        for R in range(len(prices)):
            if prices[L] > prices[R]:
                L = R
            maxProfit = max(maxProfit, prices[R] - prices[L])
        return maxProfit