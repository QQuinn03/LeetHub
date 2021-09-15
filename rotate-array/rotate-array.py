class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %=len(nums)
        length = len(nums)
        nums[:] = nums[length-k:]+nums[:length-k]


        
        
