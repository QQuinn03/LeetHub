class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        
        for i in range(len(nums)):
            if i >0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                return res
            
            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif nums[i]+nums[l]+nums[r]>0:  
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0:    
                    l+=1
        return res           
                    
                    
      
        