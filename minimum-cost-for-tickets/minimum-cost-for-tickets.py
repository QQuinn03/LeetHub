class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float("inf") for i in range(max(days)+1)]
        dp[0]=0

        price ={1:costs[0],7:costs[1],30:costs[2]}
        
        for i in range(1,len(dp)):
            if i not in days:
                dp[i]=dp[i-1]
                continue
            
            for j in [1,7,30]:
                if i>=j:
                    dp[i]=min(dp[i],dp[i-j]+price[j])
                else:
                    dp[i]=min(dp[i],dp[0]+price[j])
           
        return dp[-1]             
                
                
        
        