class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        c,d=intervals[0]
        rem=0
        for a,b in intervals[1:]:
            if d>a:
                rem+=1
                d = min(b, d)
            else:
                c,d =a,b
        return rem