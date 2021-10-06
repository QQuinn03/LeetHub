class Solution:
    def jump(self, nums: List[int]) -> int:
        step=0
        start=0
        end = 0
        cur_max = 0
        
        while end <len(nums)-1:
            step+=1
            for i in range(start,end+1):
                if i+nums[i]>=len(nums)-1:
                    return step
                cur_max=max(cur_max,i+nums[i])
            start=end+1
            end=cur_max
        return step    
            
        