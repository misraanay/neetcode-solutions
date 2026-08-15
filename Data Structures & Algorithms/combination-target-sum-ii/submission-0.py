class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        def comb(i, target, curComb):
            if target == 0:
                self.res.append(curComb.copy())
            # returns all unique combinations starting from index i onwards
            if i >= len(candidates) or candidates[i] > target:
                return
            curComb.append(candidates[i])
            comb(i+1, target - candidates[i], curComb)
            curComb.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            comb(i+1, target, curComb)
        comb(0, target, [])
        return self.res