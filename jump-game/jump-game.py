class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[False for i in range(len(nums))]
        dp[0]=True 
        current_max=0+nums[0]
        
        for i in range(1,len(nums)):
            if i>current_max:
                return False
            current_max=max(current_max,i+nums[i])
            dp[i]=True
           
        return dp[-1]    
            
        