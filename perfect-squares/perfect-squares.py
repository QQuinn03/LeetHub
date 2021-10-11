class Solution:
    def numSquares(self, n: int) -> int:
        dp=[(n+1) for i in range(n+1)]
        square=[i**2 for i in range(int(sqrt(n))+1)]
        
    
        for i in range(n+1):
            if i in square:
                dp[i]=1
            else:
                for j in square:
                    if i>j:
                        dp[i]=min(dp[i],dp[i-j]+1)
        print(dp)                
        return dp[-1]                