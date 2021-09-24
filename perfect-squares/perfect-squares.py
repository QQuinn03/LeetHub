import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        check = [i**2 for i in range(int(sqrt(n))+1)]
        dp = [(n+1) for i in range(n+1)]
        
        for i in range(len(dp)):
            for j in check:
                if i==j:
                    dp[i]=1
                elif i>j:
                    dp[i]=min(dp[i],dp[i-j]+1)
        return dp[-1]            
        
        