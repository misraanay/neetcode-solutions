class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        target = k
        for i, num in enumerate(nums):
            if i == n-1:
                return num + target
            
            btw = nums[i+1] - num - 1

            if btw >= target:
                return num + target
            target -= btw
            