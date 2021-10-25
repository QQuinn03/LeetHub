class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[False for i in range(len(nums))]
        dp[0]=True
        cur_max=0+nums[0]
        
        for i in range(1,len(nums)):
            if i >cur_max:
                return False
            dp[i]=True
            cur_max=max(cur_max,nums[i]+i)
            print(cur_max)
        return dp[-1]    
        