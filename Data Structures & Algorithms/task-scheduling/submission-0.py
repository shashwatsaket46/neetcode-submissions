from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ctr= Counter(tasks)
        mx = max(ctr.values())
        mx_ct = list(ctr.values()).count(mx)
        return max(len(tasks), (mx-1)*(n+1)+mx_ct)