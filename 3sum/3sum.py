class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        
        for i in range(len(nums)):
            if i >0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                break
            
            target=0-nums[i]
            left = i+1
            right=len(nums)-1
            while left<right:
                # print(left,right)
                if nums[left]+nums[right]==target:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif nums[left]+nums[right]<target:
                    left+=1
                elif nums[left]+nums[right]>target:
                    right-=1
        return res            
                        
                    
                    
                
                