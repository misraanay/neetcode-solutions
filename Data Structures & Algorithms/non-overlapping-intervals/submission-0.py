class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0]
        num = 0

        for i, pair in enumerate(intervals):
            if i == 0:
                continue
            if prev[1] <= pair[0]:
                prev = pair
                continue
            else:
                num += 1
                prev = [max(prev[0], pair[0]), min(pair[1], prev[1])]
        return num


        