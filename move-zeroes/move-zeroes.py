class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx_zero = 0
        idx = 0
        
        for i in range(len(nums)):
            if nums[i]==0:
                pass
            else:
                nums[idx_zero],nums[i]=nums[i],nums[idx_zero]
                idx_zero+=1
                
                