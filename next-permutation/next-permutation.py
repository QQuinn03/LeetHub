class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx=len(nums)-2
        while idx>=0 and nums[idx]>=nums[idx+1]:
            idx-=1
        if idx==-1:
            print(idx)
            return nums.sort()
        change=idx+1
        
        while change<len(nums) and nums[change]>nums[idx]:
            change+=1
        change-=1
        
        nums[idx],nums[change]=nums[change],nums[idx]
        nums[idx+1:]=sorted(nums[idx+1:])
        print(nums)
        return nums
        
        