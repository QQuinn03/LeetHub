class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp=[float("inf") for i in range(max(days)+1)]
        dp[0]=0
        prices={1:costs[0],7:costs[1],30:costs[2]}
        
        for i in range(1,len(dp)):
            if i not in days:
                dp[i]=dp[i-1]
            else:
                for price in prices:
                    val=prices[price]
              
                    dp[i]=min(dp[i],dp[max(i-price,0)]+val)
        print(dp)        
        return dp[-1]           