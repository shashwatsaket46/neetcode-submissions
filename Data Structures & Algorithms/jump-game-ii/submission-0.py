class Solution:
    def jump(self, nums: List[int]) -> int:
        start=0
        curr=0
        far=0
        for i in range(len(nums)-1):
            far = max(far, i+nums[i])
            if i==curr:
                start+=1
                curr =far
        return start