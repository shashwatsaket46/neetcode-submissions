from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ct = Counter(nums)
        for key, val in ct.items():
            heapq.heappush(heap, [val, key])
            if len(heap)>k:
                heapq.heappop(heap)
        return [key for val, key in heap]
### Sabse optimized ye wali hai, isme ek counter mein sab element daal diye, phir heap mein har element ko daalte gye, aur jab bhi heap ki length k se jyada hui, heap ko pop karte gye, iske baad jab end hui, toh key ko return karwa diye ASAF.