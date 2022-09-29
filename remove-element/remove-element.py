class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx1=0
        idx2=0
        
        while idx2<len(nums):
            if nums[idx2]!=val:
                nums[idx1]=nums[idx2]
                idx1+=1
                idx2+=1
            else:
                idx2+=1
        
        return idx1
        