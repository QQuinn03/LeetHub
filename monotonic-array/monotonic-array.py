class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag1=False
        flag2=False
        
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                flag1=True
            if nums[i]>nums[i-1]:
                flag2=True
            
            if flag1 and flag2:
                return False
        return True     
        