class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n =  len(nums)
        dp = [0] * n
        dp[n-1] = 1

        for i in range(n-2, -1 , -1):
            for j in range(i+1, n):
                if dp[j] > dp[i] and nums[j] > nums[i]:
                    dp[i] = dp[j]
            dp[i] += 1
        return max(dp)