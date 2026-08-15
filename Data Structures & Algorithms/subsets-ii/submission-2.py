class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def back(i, curSub):
            if i >= len(nums):
                res.append(curSub.copy())
                return
            #include
            curSub.append(nums[i])
            back(i+1, curSub)
            curSub.pop()

            #exclude - skip to the next number
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            back(i+1, curSub)

        back(0, [])
        return res




        
        