from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d =Counter(nums)
        return True if len(d)<len(nums) else False
