import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        heap=[]
        for i in range(len(points)):
            x,y = points[i]
            dist = x**2 +y**2
            heap.append((dist, [x,y]))
        heapq.heapify(heap)
        for i in range(k):
            dist, pt = heapq.heappop(heap)
            ans.append(pt)
        return ans