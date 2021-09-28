class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            self.helper(nums,i,res)
        return res
    
    def helper(self,nums,i,res):
        j = i+1
        seen = set()
        while j<len(nums):
            
            target=-(nums[i]+nums[j])
            if target in seen:
                res.append([nums[i],nums[j],target])
                while j+1<len(nums) and nums[j]==nums[j+1]:
                    j+=1
            seen.add(nums[j])    
            j+=1     

       
        