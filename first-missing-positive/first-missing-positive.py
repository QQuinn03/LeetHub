class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        nums.sort()
        
        res=nums[-1]
        idx=0
        for i in range(len(nums)):
            if nums[i]<=0:
                continue
            elif nums[i]>0:
                temp=nums[i]
                idx=i
                break
        print(idx,temp)        
        for i in range(idx+1,len(nums)):
            if temp==nums[i]:
                continue
            if temp+1<nums[i]:
                return temp+1
            temp+=1
        return nums[-1]+1    
            
                
       