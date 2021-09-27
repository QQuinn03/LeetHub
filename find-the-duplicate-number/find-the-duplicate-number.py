class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicate=0
        for num in nums:
            idx = abs(num)
          
            if nums[idx]<0:
                duplicate=idx
            nums[idx]=-nums[idx] 
        return duplicate    