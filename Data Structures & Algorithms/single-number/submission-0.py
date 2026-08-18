class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt=0
        for x in nums:
            cnt^= x
        return cnt