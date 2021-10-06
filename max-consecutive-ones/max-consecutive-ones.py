class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        left=0
        right = 0
        while right<len(nums):
            if nums[right]==1:
                res=max(res,right-left+1)
            else:
                left=right+1
            right+=1     
        return res        