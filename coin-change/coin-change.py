class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [(amount+1) for i in range(amount+1)]
        dp[0]=0
        # dp[1]=1
              
        for i in range(1,len(dp)):
              if i in coins:
             
                    dp[i]=1
                
              for j in coins:
                if i>j:
                  
                    dp[i]=min(dp[i],dp[i-j]+1)
                
        if dp[-1]==amount+1:     
              return -1
        return dp[-1]      