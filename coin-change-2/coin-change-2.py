class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount+1)]
        dp[0]=1
        
        for i in coins:
            for j in range(1,len(dp)):
                if j==i:
                    dp[j]+=1
                if j>i:
                    dp[j]+=dp[j-i]
        return dp[-1]            