class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pp=1
        ans=[1]*len(nums)
        for i in range(len(nums)):
            ans[i]=pp
            pp*=nums[i]
        sp=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=sp
            sp*=nums[i]
        return ans
        