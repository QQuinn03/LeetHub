class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("inf") for i in range(amount+1)]
        dp[0]=0
        
        for i in range(1,len(dp)):
            for j in coins:
                if i>=j:
                    dp[i]=min(dp[i],dp[i-j]+1)
        if dp[-1]==float("inf"):
            return -1
        return dp[-1]            