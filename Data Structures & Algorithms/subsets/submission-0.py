class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsets = []

        def sub(i, curSub):
            if i >= len(nums):
                self.subsets.append(curSub.copy())
                return
            
            # do not include
            sub(i+1, curSub.copy())
            curSub.append(nums[i])
            sub(i+1, curSub.copy())

        sub(0, [])
        return self.subsets

    
""" pseudocode 

for every number take the crrent sub set and make two recursive calls, in one add the the number in the other dont

"""