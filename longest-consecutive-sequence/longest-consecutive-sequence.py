class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        res=1
        temp=1
        
        for i in range(1,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if i>0 and nums[i]-nums[i-1]==1:
                temp+=1
                
            
                
                if temp>res:
                    res=temp
            else:        
                temp=1 
                
        return res        
   