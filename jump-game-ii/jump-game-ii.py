class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        cur_max=0
        start=0
        end = 0
        
        for i in range(len(nums)-1):
            step+=1
            for j in range(start,end+1):
                if nums[j]+j>=len(nums)-1:
                    return step
                cur_max=max(cur_max,nums[j]+j)
            start=end+1
            end=cur_max
        return step  
            
         
            
        