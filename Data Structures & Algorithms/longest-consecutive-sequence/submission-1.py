class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)

        res = 0
        for num in nums:
            if num - 1 not in hashset:
                count = 0
                cur = num
                while cur in hashset:
                    count += 1
                    cur += 1
                res = max(res, count)
        return res

