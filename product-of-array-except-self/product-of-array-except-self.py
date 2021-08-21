class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        val = 1
        res = []
        
        for i in range(len(nums)):
            res.append(val)
            val *=nums[i]
         
        val = 1
        
        for i in range(len(nums)-1,-1,-1):
            res[i]*=val
            val*=nums[i]
        return res     