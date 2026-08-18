class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()
        s_q = sorted(queries)
        ans={}
        heap=[]
        i=0
        for q in s_q:
            while i<len(intervals) and intervals[i][0]<=q:
                a,b =intervals[i]
                length = b-a+1
                heapq.heappush(heap, (length, b))
                i+=1
            while heap and heap[0][1]<q:
                heapq.heappop(heap)
            if heap:
                ans[q] =heap[0][0]
            else:
                ans[q]=-1
        return [ans[i] for i in queries]
