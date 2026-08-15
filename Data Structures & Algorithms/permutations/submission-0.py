class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutations(i):
            if i == len(nums) - 1:
                return [[nums[i]]]
            perms = list(permutations(i+1))
            res = []
            for perm in perms:
                for j in range(len(perm) + 1):
                    nperm = perm.copy()
                    nperm.insert(j, nums[i])
                    res.append(nperm)
            return res
        return permutations(0)