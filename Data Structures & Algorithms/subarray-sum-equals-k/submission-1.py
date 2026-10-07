class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        premap = {}
        res = 0
        premap[0] = 1 # the way to ensure that full array is considered in chopping
        total = 0
        for i, num in enumerate(nums):
            total += num
            res += premap.get(total - k, 0)
            premap[total] = premap.get(total, 0) + 1
        return res 





        