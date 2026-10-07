class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]

        # now we know there is atleast one target
        

        #
        n = len(nums)
        lowest = n+1
        l, r = 0, n - 1

        while l <= r:
            m = (l+r) // 2

            if nums[m] < target:
                l = m+1
            else:
                r = m-1
                if nums[m] == target:
                    lowest = min(lowest, m)
        
        highest = -1
        l, r = 0, n - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] <= target:
                l = m+1
                if nums[m] == target:
                    highest = max(highest, m)  
            else:
                r = m-1
        
        return [lowest, highest]
        