from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ct = Counter(nums)
        for key, val in ct.items():
            heapq.heappush(heap, [-val, key])
        heapq.heapify(heap)
        ans=[]
        for _ in range(k):
            k, v= heapq.heappop(heap)
            ans.append(v)
        return ans