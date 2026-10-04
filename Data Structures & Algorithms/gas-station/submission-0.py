class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total = 0
        diff_arr = [g-c for g,c in zip(gas, cost)]
        if sum(diff_arr) < 0:
            return - 1
        res = 0
        for i, diff in enumerate(diff_arr):
            total += diff
            if total < 0:
                total = 0
                res = i + 1
        return res