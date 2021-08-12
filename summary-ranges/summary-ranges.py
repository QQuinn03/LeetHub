class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return nums
        nums = nums + [nums[-1]+2] 
        head = nums[0]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>1:
                if head ==nums[i-1]:
                    res.append(str(head))
                else:
                    res.append(str(head)+"->"+str(nums[i-1]))
                head = nums[i]
        return res    
                
                
        
        
                    
                
                
                
                