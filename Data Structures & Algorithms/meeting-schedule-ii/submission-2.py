"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])
        res = 0
        l, r = 0, 0
        count = 0
        while l < n or r < n:
            if l >= n or min(starts[l], ends[r]) == ends[r]:
                val = ends[r]
                count -= 1
                r+=1
            elif r >= n or min(starts[l], ends[r]) == starts[l]:
                val = starts[l]
                count += 1
                l += 1

            res = max(res, count)
        return res

