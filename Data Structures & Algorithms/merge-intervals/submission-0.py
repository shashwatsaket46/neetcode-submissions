class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        c,d =intervals[0]
        ans=[]
        for a,b in intervals[1:]:
            if a>d:
                ans.append([c,d])
                c,d =a,b
            else:
                c =min(a,c)
                d=max(b,d)
        ans.append([c,d])
        return ans