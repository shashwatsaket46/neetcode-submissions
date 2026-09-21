from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k =Counter(s)
        l = Counter(t)
        return k==l