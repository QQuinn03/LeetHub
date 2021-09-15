class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set=set(nums)
        
        for val in range(len(nums)+1):
            if val not in nums_set:
                return val