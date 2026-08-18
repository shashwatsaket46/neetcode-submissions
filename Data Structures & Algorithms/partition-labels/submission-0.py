class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start=0
        curr=0
        lst={}
        for i in range(len(s)):
            lst[s[i]]=i
        ans=[]
        for i in range(len(s)):
            curr = max(curr, lst[s[i]])
            if i==curr:
                ans.append(curr-start+1)
                start=i+1
        return ans