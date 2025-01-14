class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("inf") for i in range(amount+1)]
        dp[0]=0
        
        for i in range(len(dp)):
            if i in coins:
                dp[i]=1
            for coin in coins:
                if i>coin:
                    dp[i]=min(dp[i],dp[i-coin]+1)
        if dp[-1]==float("inf"):
            return -1
        return dp[-1]            