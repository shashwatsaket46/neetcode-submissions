class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pp =1
        
        ans=[1]*len(nums)
        for i in range(len(nums)):
            ans[i] = pp
            pp*=nums[i]
        sp=1
        for j in range(len(nums)-1,-1,-1):
            ans[j]*=sp
            sp*=nums[j]
        return ans
