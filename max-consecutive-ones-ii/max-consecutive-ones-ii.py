class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one=0
        left=0
        right=0
        res=0
        
        while right<len(nums):
            if nums[right]==1:
                pass
            if nums[right]==0:
                one+=1
            while one>1:
                if nums[left]==0:
                    one-=1
                left+=1
            res=max(res,right-left+1)
            right+=1
        return res     