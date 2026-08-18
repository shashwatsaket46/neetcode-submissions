"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key= lambda x: x.start)
        heap=[]
        for i in intervals:
            a=i.start
            b=i.end
            if heap and heap[0]<=a:
                heapq.heappop(heap)
            heapq.heappush(heap, b)
        return len(heap)

        
