class Solution:
    def numSquares(self, n: int) -> int:
        if n==1:
            return n
        dp=[(n+1) for i in range(n+1)]
        sq=[i**2 for i in range(int(sqrt(n))+1)]

        for i in range(len(dp)):
            if i in sq:
                dp[i]=1
            else:
                for j in sq:
                    if i>j:
                        dp[i]=min(dp[i],dp[i-j]+1)
             
        return dp[-1]            
