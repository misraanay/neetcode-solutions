class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            m = (l+r) // 2
            if nums[l] >= nums[r]:
                if nums[l] <= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                r = m - 1
            res = min(res, nums[m])
        return res