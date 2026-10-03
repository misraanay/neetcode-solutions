class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            if nums[i] == 0:
                continue
            k = min(i + nums[i], n-1)
            dp[i] = 1 + min(dp[j] for j in range(i+1, k+1))
        return dp[0]