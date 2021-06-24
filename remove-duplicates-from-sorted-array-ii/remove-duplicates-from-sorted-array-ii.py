class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count  = 1
        i = 0
        
        while i <len(nums)-1:
            if nums[i]!=nums[i+1]:
                count=1
                
            else:
                count+=1
                if count==2:
                    i+=1
                    continue
                else:
                    del nums[i]
                    continue    
            i+=1        