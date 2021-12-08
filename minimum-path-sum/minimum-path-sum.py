class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        dp[0][0]=grid[0][0]
    
        row=len(grid)
        col=len(grid[0])
        
        for i in range(1,col):
            dp[0][i]=dp[0][i-1]+grid[0][i]
       
        for j in range(1,row):
            dp[j][0]=dp[j-1][0]+grid[j][0]
        
        for i in range(1,row):
            for j in range(1,col):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[-1][-1]        
        
        
        
   