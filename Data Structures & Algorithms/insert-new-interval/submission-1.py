class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, pair in enumerate(intervals):
            if newInterval[1] < pair[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > pair[1]:
                res.append(pair)
            else:
                newInterval = [min(pair[0], newInterval[0]), max(pair[1], newInterval[1])]
        
        res.append(newInterval)
        return res
        