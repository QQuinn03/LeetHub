class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for i in range(len(cost)+1)]
        for i in range(2,len(dp)):
            step_one = dp[i-1]+cost[i-1]
            step_two = dp[i-2]+cost[i-2]
            dp[i]= min(step_one,step_two)
        return dp[-1]    
        
            
        