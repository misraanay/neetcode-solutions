class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums)
        dp = [max(nums[-2:]), nums[-1]]

        for i in range(l-2):
            temp = dp[0]
            dp[0] = max(nums[l-3-i]+ dp[1], dp[0])
            dp[1] = temp
        return dp[0]
            


        
        
        