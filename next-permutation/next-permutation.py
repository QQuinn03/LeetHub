class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #1 2 6 4 2
        #nums[i]<nums[i+1] 2
        #[6 4 2] cloest to 2   4
        #14226
        
        idx = len(nums)-2
        
        while idx!=-1:
            if nums[idx]>=nums[idx+1]:
                idx-=1
            else:
                break
        if idx ==-1:
           
            return nums.sort()
        print(idx)
        change = idx+1
        while change<len(nums) and nums[change]>nums[idx]:
            change+=1
            
        change-=1
        print(change)
        nums[idx],nums[change]=nums[change],nums[idx]
        nums[idx+1:]=sorted(nums[idx+1:])
        return nums
        
        