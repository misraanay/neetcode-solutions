class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = False
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i]== nums[j]:
                    found = True
        return found
         