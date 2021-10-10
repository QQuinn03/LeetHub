class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        dp = [[1 for i in range(col)]for j in range(row)]
        
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
        
        for j in range(0,col-1):
                if dp[0][j]==0:
                    dp[0][j+1]=0
        for i in range(row-1):
            if dp[i][0]==0:
                dp[i+1][0]=0
        for i in range(1,row):
            for j in range(col):
                if dp[i][j]==0:
                    continue
                if j ==0:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]            