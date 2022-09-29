class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx1=0
        idx2=0
        while idx2<len(nums):
            if nums[idx2]==nums[idx1]:
                idx2+=1
            else:
                idx1+=1
                nums[idx1]=nums[idx2]
                idx2+=1
        return idx1+1
            