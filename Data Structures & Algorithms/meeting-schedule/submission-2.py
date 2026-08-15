"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True
        intervals.sort(key = lambda x: x.start)

        n = len(intervals)

        prev = intervals[0]

        for i, interval in enumerate(intervals):
            if i == 0:
                continue
            if prev.end <= interval.start:
                prev = interval
            else:
                return False

        return True




