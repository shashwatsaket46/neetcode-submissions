from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = Counter(s)
        e = Counter(t)
        return d==e