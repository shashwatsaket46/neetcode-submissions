from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ctr= Counter(tasks)
        # mx = max(ctr.values())
        # mx_ct = list(ctr.values()).count(mx)
        # return max(len(tasks), (mx-1)*(n+1)+mx_ct)
        ctr = Counter(tasks)
        heap = [-freq for freq in ctr.values()]
        heapq.heapify(heap)
        q =deque()
        time=0
        while q or heap:
            time+=1
            if heap:
                freq = heapq.heappop(heap)
                freq+=1
                if freq!=0:
                    q.append((freq, time+n))
            if q and q[0][1]==time:
                freq, _ =q.popleft()
                heapq.heappush(heap, freq)
        return time









