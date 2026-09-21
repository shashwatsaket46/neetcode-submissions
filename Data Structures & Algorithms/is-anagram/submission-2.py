from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt={}
        for c in s:
            cnt[c] = cnt.get(c,0)+1
        for k in t:
            cnt[k]=cnt.get(k,0)-1
        return all(v==0 for v in cnt.values())
