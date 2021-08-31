class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount+1)]
        dp[0]=1
        
        for i in coins:
            for j in range(len(dp)):
                if j==i:
                    dp[j]+=1
                if j>i:
                    dp[j]+=dp[j-i]
        if dp[-1]==0:
            return 0

        return dp[-1]