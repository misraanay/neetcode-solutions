class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        old = intervals[0]
        res = []

        for i, pair in enumerate(intervals):
            if i == 0:
                continue
            if old[1] < pair[0]:
                res.append(old)
                old = pair
            else:
                old = [min(old[0], pair[0]), max(old[1], pair[1])]
        res.append(old)
        return res







