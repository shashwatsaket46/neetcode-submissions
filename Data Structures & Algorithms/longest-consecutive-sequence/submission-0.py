class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st =set(nums)
        mx=0
        for n in st:
            if n-1 not in st:
                l=1
                while n +l in st:
                    l+=1
                mx =max(mx, l)
        return mx