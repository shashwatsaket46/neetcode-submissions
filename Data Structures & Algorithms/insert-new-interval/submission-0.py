class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        c,d =newInterval
        ans=[]
        for a, b in intervals:
            if d <a:
                ans.append([c,d])
                c,d=a,b
            elif c>b:
                ans.append([a,b])
                
            else:
                c= min(a,c)
                d=max(b,d)
        ans.append([c,d])

        return ans
