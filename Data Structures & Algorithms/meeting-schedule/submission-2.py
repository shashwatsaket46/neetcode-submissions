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
        intervals.sort(key=lambda x: x.start)
        prev = intervals[0].end
        for a in intervals[1:]:
            if a.start<prev:
                return False
            else:
                prev =a.end
        return True
