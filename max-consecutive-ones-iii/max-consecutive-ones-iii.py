class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = 0
        ks = 0
        res = 0
        
        while right<len(nums):
            if nums[right]==1:
                pass
            if nums[right]==0:
                ks+=1
            while ks>k:
                start=nums[left]
                if start==0:
                    ks-=1
                left+=1
            res = max(res,right-left+1)
            right+=1
        return res     
                    