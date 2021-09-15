class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        idx = len(nums)-2
      
        while idx>=0 and nums[idx]>=nums[idx+1]:
            idx-=1
            
        if idx==-1:
            return nums.reverse()
        change = idx+1
        
        while change<len(nums) and nums[change]>nums[idx]:
            change+=1
        
        change-=1
        nums[idx],nums[change]=nums[change],nums[idx]
        print(nums)
        nums[idx+1:]=sorted(nums[idx+1:])
        return nums
        