class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur_max=0
        for i in range(len(nums)):
            if cur_max<i:
                return False
            cur_max=max(cur_max,nums[i]+i)
        return True    