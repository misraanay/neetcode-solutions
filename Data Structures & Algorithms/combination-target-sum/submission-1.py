class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        self.res = []
        
        def combinations(i, curSub, curSum):
            if curSum > target:
                return
            if curSum == target:
                self.res.append(curSub.copy())
                return
            if i >= len(nums):
                return
            
            # either add the ith number or move on to the next one
            curSum+=nums[i]
            curSub.append(nums[i])
            combinations(i, curSub, curSum)
            curSub.pop()
            
            curSum -= nums[i]
            combinations(i+1, curSub, curSum)

        combinations(0, [], 0)
        return self.res

        