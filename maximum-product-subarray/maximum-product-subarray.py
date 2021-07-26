class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = nums[0]
        cur_max = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            temp = cur_min
            cur_min = min(nums[i],cur_min*nums[i],cur_max*nums[i])
           
            cur_max = max(nums[i],temp*nums[i],cur_max*nums[i])
            
            res = max(res,cur_max)
        return res    
        