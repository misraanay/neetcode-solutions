class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        pos = 0

        while pos < n:
            if pos == n-1:
                return True
            if nums[pos] == 0:
                return False
            maxjump = 0
            jump = 0
            for i in range(1, nums[pos]+1):
                if i + pos < n and i + nums[i+pos] > maxjump:
                    jump = i
                    maxjump = i + nums[i+pos]
            pos += jump
