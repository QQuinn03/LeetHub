class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = m
        col =n
        dp=[[1 for i in range(col)]for j in range(row)]
        
        for i in range(1,row):
            for j in range(1,col):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]        