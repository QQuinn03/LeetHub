class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_ = set(nums)
        res = (3*sum(set_)-sum(nums))//2
        return res